# EvoLoop: Technical Architecture

To build a robust Idle game in Unity—especially one that needs to simulate potentially thousands of interactions per second and calculate offline progress instantly—the **Game Logic** must be completely decoupled from the **Visual Rendering**. 

If damage calculations rely on Unity's physical colliders or `Update()` framerate, the game will lag heavily, and calculating offline progress will be impossible. This document outlines the **Tick-Based Simulation** model for EvoLoop.

## 1. The Architectural Philosophy: Logic vs. View
*   **The Model (Data):** Pure C# classes (not `MonoBehaviour`s). They hold the stats for the Digital Ghost, the Corporate ICE, and the active Mutations.
*   **The Controller (Simulation Engine):** A central manager that manually "ticks" the game logic forward by a specific amount of time.
*   **The View (Visuals):** Unity `MonoBehaviour`s that just look at the Model and update their position, VFX, or UI based on what the Model says.

## 2. Core Game Loop Architecture

### A. The Simulation Engine (The Heartbeat)
This script controls the flow of time. Because time is passed as a `deltaTime` variable, it can accept `0.016f` for live gameplay, or `86400f` (24 hours) broken into chunks to instantly simulate offline progress when the player opens the app.

```csharp
using System.Collections.Generic;
using UnityEngine;

public class SimulationEngine : MonoBehaviour
{
    public GhostEntity PlayerGhost;
    public WaveManager WaveSystem;
    public CombatEngine Combat;
    public SynergyManager Synergies;

    private float _runTimer = 0f;
    private bool _isRunning = false;

    public void StartRun(List<TraitData> selectedTraits, PhilosophyData philosophy)
    {
        PlayerGhost = new GhostEntity(selectedTraits, philosophy);
        WaveSystem.Reset();
        _runTimer = 0f;
        _isRunning = true;
    }

    // Standard Unity Update for live viewing
    private void Update()
    {
        if (_isRunning)
        {
            TickSimulation(Time.deltaTime);
        }
    }

    // The actual core loop. 
    // This can be called repeatedly in a while-loop to calculate offline progress!
    public void TickSimulation(float delta)
    {
        _runTimer += delta;

        // 1. Spawn new Corporate ICE or Logic Gates based on the timer
        WaveSystem.Tick(delta, _runTimer);

        // 2. Trigger passive Aura / Synergies (e.g. Necro-Hacker summons, Hex-Code pulses)
        Synergies.Tick(delta, PlayerGhost, WaveSystem.ActiveEnemies);

        // 3. Process auto-attacks and damage
        Combat.ProcessAttacks(delta, PlayerGhost, WaveSystem.ActiveEnemies);

        // 4. Clean up dead ICE and collect Biomass
        ProcessDeathsAndBiomass();

        // 5. Check Lose State
        if (PlayerGhost.CurrentHP <= 0)
        {
            TriggerCompileError(); // The run collapses
        }
    }

    private void ProcessDeathsAndBiomass()
    {
        float biomassGained = WaveSystem.ClearDeadEnemies();
        if (biomassGained > 0)
        {
            PlayerGhost.AddBiomass(biomassGained);
            if (PlayerGhost.CanMutate())
            {
                // Pause simulation, open Draft UI for new Mutation
                _isRunning = false; 
                UIManager.Instance.ShowMutationDraft();
            }
        }
    }
    
    private void TriggerCompileError()
    {
        _isRunning = false;
        // Handle run failure and distribute Fragments of Truth (meta-currency)
    }
}
```

### B. The Entity Model (Pure Data)
Notice this is *not* a `MonoBehaviour`. This allows it to live purely in memory, making the simulation incredibly fast.

```csharp
using System.Collections.Generic;

public class GhostEntity
{
    // Base Stats
    public float MaxHP { get; private set; }
    public float CurrentHP { get; private set; }
    public float BaseDamage { get; private set; }
    public float AttackSpeed { get; private set; }
    public float Biomass { get; private set; }

    public List<MutationData> ActiveMutations = new List<MutationData>();

    public GhostEntity(List<TraitData> startingTraits, PhilosophyData philosophy)
    {
        // Initialize base stats
        MaxHP = 100f;
        CurrentHP = MaxHP;
        BaseDamage = 10f;

        // Apply Trait Modifiers (e.g., "Soul-Bound SLA" sets MaxHP to 1, Damage to +200%)
        foreach(var trait in startingTraits)
        {
            trait.ApplyToEntity(this);
        }

        // Apply Philosophy Rules
        philosophy.ApplyRuleChanges(this);
    }

    public void TakeDamage(float amount)
    {
        CurrentHP -= amount;
    }

    public void AddBiomass(float amount)
    {
        Biomass += amount;
    }
    
    public bool CanMutate()
    {
        // Math to check if Biomass exceeds the current level threshold
        return Biomass >= CalculateNextThreshold();
    }
    
    private float CalculateNextThreshold()
    {
        // Example scaling math
        return (ActiveMutations.Count + 1) * 100f; 
    }
}
```

### C. The Synergy & Data Layer (ScriptableObjects)
In Unity, `ScriptableObjects` should be used to define Traits, Mutations, and Truth Cards. This allows for the rapid creation of hundreds of variations (or AI generation of them) without touching the core code.

```csharp
using UnityEngine;
using System.Collections.Generic;

[CreateAssetMenu(fileName = "NewTrait", menuName = "EvoLoop/Trait")]
public class TraitData : ScriptableObject
{
    public string TraitName;
    [TextArea] public string LoreText; // e.g., "Ghost-Log 114..."
    
    // Tags for the Synergy Engine to weight RNG drafts
    public List<string> SynergyTags; 

    // Abstract method that specific Traits override to alter stats
    public virtual void ApplyToEntity(GhostEntity entity)
    {
        // Example: Base implementation does nothing
    }
}
```

## 3. Handling Visuals (The "Screensaver")
Since the `SimulationEngine` handles all the math, the visual layer just needs to interpret it. 

For example, you would create a `GhostVisuals.cs` `MonoBehaviour` attached to the glowing Tesseract/Core in your Unity scene. Every frame, it asks the `SimulationEngine` for the `PlayerGhost.CurrentHP` to adjust its glow intensity, or listens to an event when the `CombatEngine` fires an attack to trigger a Unity VFX Graph particle burst.

### Why this architecture is perfect for EvoLoop:
1.  **Offline Calculations:** When the user returns after 12 hours, the game can run a `while` loop that calls `TickSimulation(1.0f)` 43,200 times. Because there are no visual updates or physics colliders slowing it down, it will calculate an entire day of idle surviving and dying in a fraction of a second.
2.  **Infinite Scaling:** Since stats are just raw variables (not tied to physical rigidbodies), if the *Chrome Martyr* trait gives the player 10 billion armor, the game won't crash.
3.  **Active Variant Compatibility:** If you build the "Active" version of the game, you use this *exact same* `GhostEntity` and `SimulationEngine`. The only difference is that you add a `JoystickController.cs` that moves the player's X/Y coordinates in the Model!