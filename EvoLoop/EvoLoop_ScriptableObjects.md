---
layout: default
title: EvoLoop ScriptableObjects
permalink: /evoloop/scriptable-objects/
sitemap: false
---
# EvoLoop: ScriptableObject Framework

This document outlines the C# `ScriptableObject` architecture used to define the core data for Traits and Mutations in EvoLoop. By abstracting item data into ScriptableObjects, designers can rapidly prototype new synergies in the Unity Editor without altering code.

## 1. The Stat System
To make the synergy engine infinitely scalable, we need a generic way to define stat changes rather than hardcoding variables for every single item.

```csharp
using UnityEngine;

public enum StatType
{
    MaxHP,
    BaseDamage,
    AttackSpeed,
    MovementSpeed,
    Armor,
    AreaOfEffect,
    CollectionRadius
}

[System.Serializable]
public class StatModifier
{
    public StatType Stat;
    [Tooltip("Added directly to the base stat (e.g. +10 Damage)")]
    public float FlatValue;
    [Tooltip("Percentage multiplier (e.g. 0.5 = +50%) applied after flat values")]
    public float Multiplier; 
}
```

## 2. TraitData (Starting Archetypes)
Traits are chosen before the run. They set the entity's foundation and inject specific tags into the RNG pool to weight the draft.

```csharp
using UnityEngine;
using System.Collections.Generic;

[CreateAssetMenu(fileName = "NewTrait", menuName = "EvoLoop/Trait")]
public class TraitData : ScriptableObject
{
    [Header("Lore & UI")]
    public string TraitName;
    [TextArea] public string LoreText;
    public Sprite Icon;

    [Header("Synergy Tags")]
    [Tooltip("Tags injected into the RNG pool (e.g., 'Minion', 'Aura')")]
    public List<string> SynergyTags;

    [Header("Base Modifiers")]
    public List<StatModifier> Modifiers;

    // Virtual method allows complex traits to attach custom MonoBehaviours or event listeners
    // e.g., 'Hex-Code Anomaly' could override this to subscribe to the TakeDamage event
    public virtual void InitializeTrait(GhostEntity entity)
    {
        // Base implementation does nothing
    }
}
```

## 3. MutationData (Mid-Run Upgrades)
Mutations are drafted during the run. They contain multiple "Levels," allowing the player to upgrade them for escalating power.

```csharp
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class MutationLevel
{
    [TextArea] public string LevelDescription;
    public List<StatModifier> Modifiers;
}

[CreateAssetMenu(fileName = "NewMutation", menuName = "EvoLoop/Mutation")]
public class MutationData : ScriptableObject
{
    [Header("Lore & UI")]
    public string MutationName;
    public Sprite Icon;

    [Header("Drafting Rules")]
    public int RarityTier = 1;
    [Tooltip("Only shows up in draft if the player has these tags")]
    public List<string> RequiredTags;

    [Header("Progression")]
    public int MaxLevel => Levels.Count;
    public List<MutationLevel> Levels;
}
```

## 4. Meta-Progression (Truth Cards & Rebirth)
To handle the overarching narrative and the "Sacred Core" skill tree, we need data structures that represent unlockable lore events and permanent progression nodes.

```csharp
using UnityEngine;
using System.Collections.Generic;

[CreateAssetMenu(fileName = "NewTruthCard", menuName = "EvoLoop/Truth Card")]
public class TruthCardData : ScriptableObject
{
    [Header("Lore (Daemon-Log)")]
    public string CardTitle; // e.g., "The Concept of Theft"
    [TextArea] public string LogText; // e.g., "Ghost-Log 114: The entity observed..."
    
    [Header("Unlock Requirements")]
    [Tooltip("Text explaining how to unlock this to the player.")]
    public string RequirementDescription; // e.g., "Survive for 10 minutes."
    
    [Header("Rewards")]
    [Tooltip("A description of the mechanic unlocked.")]
    public string RewardDescription; // e.g., "Unlocks: Parasitic Drain (Lifesteal)"
    
    [Tooltip("The actual ScriptableObject unlocked (TraitData, MutationData, Arena, etc.)")]
    public ScriptableObject UnlockedAsset; 
}

[CreateAssetMenu(fileName = "NewMetaUpgrade", menuName = "EvoLoop/Meta Upgrade (Rebirth Node)")]
public class MetaUpgradeData : ScriptableObject
{
    [Header("Node Info")]
    public string NodeName;
    public int FragmentCost;
    public Sprite NodeIcon;

    [Header("Dependencies")]
    public List<MetaUpgradeData> PrerequisiteNodes;

    [Header("Permanent Buffs")]
    public List<StatModifier> PermanentModifiers;
    
    [Header("System Unlocks")]
    public int BanishChargesAdded;
    public int RerollChargesAdded;
    public int SkipChargesAdded;
}

[CreateAssetMenu(fileName = "NewPhilosophy", menuName = "EvoLoop/Philosophy")]
public class PhilosophyData : ScriptableObject
{
    [Header("Lore & UI")]
    public string PhilosophyName;
    [TextArea] public string Description;
    public int SynthesisCost; // Fragments required to form this philosophy
    
    // Abstract method to apply game-breaking rules (like disabling XP drops for 'Philosophy of Consumption')
    public virtual void ApplyRuleChanges(GhostEntity entity)
    {
        // Base implementation does nothing
    }
}
```