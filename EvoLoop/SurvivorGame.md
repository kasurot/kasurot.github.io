---
layout: default
title: EvoLoop Game Design
permalink: /evoloop/design/
sitemap: false
---
# Project Placeholder: "EvoLoop" (Active & Idle Variants)

## 🎯 1. The Core Concept
A minimalist, highly synergistic roguelike where you construct a build and watch it clash against endless waves. The game strips away bloated exploration in favor of pure, hypnotic combat and deep meta-progression. 

To capture the widest audience, the game will be designed around a dual-variant strategy:
*   **Variant A (The Idle Roguelike):** 100% auto-battling. You set the rules, mutations, and philosophies, press "Start," and sit back. Perfect for the second-monitor/incremental game audience.
*   **Variant B (The Active Roguelike):** *Vampire Survivors*-style movement or twin-stick aiming. You manually dodge, collect Soul-Data (via a Magnetism stat), and trigger ultimate abilities while auto-firing. Perfect for the action-roguelite audience.
*   *Dev Advantage:* Both games use the exact same backend stats, enemies, narrative, and progression systems. Only the input controller and targeting AI change.

## 🔄 2. The Core Loop
The loop is designed to be fast, rewarding, and inevitable in its collapse.
1.  **Draft:** Choose a starting build direction combining:
    *   *Traits:* Baseline stat modifiers (e.g., "Glass Cannon," "Regenerator").
    *   *Mutations:* Mid-run evolutionary choices and explicit *Fusions* (combining max-level mutations for super-tier abilities).
    *   *Philosophies:* Meta-progression stances (e.g., "The Way of the Swarm," "The Path of the Monolith").
2.  **Execute (Press Start):** The entity enters the single arena. 
3.  **Witness/Act:** 
    *   *Idle Variant:* Watch the mesmerizing chaos unfold.
    *   *Active Variant:* Steer the entity, scoop up scattered Soul-Data, and dodge Logic Gates.
4.  **Collapse:** The run inevitably fails as the system gets overwhelmed.
5.  **Rebirth:** Spend accumulated resources to unlock permanent upgrades, expanding the sandbox for the next run.

## 👀 3. The "Watching" Layer (Visuals & Hook)
The game must look like a beautiful, chaotic screensaver. The cognitive load should be incredibly low to parse, but deep to master.
*   **Dynamic Arenas (Biomes):** Multiple high-contrast settings (e.g., dark neon void, overgrown synthetic ruins, crystalline data-caverns). While visually distinct, all arenas adhere to the rule of "no confusing walls or mazes" to maintain focus on the combat. Arenas can be unlocked via progression or acquired as cosmetic skins.
    *   *The Neon Construct (Starting):* Deep black void with a pulsing cyan wireframe floor inscribed with ancient magical runes. Pure, readable contrast.
    *   *The Chrome Cathedral:* Towering silver spires of a Megacorporation's data-vault, lit by stained-glass holographic windows.
    *   *The Neon Slums:* Rainy, holographic alleyways where the system's "junk data" and forgotten digital ghosts reside.
    *   *The Molten Forge:* Charcoal-black grates suspended over rivers of searing orange plasma.
    *   *The Corrupted Sector:* Visually unstable dataspace with chromatic aberration and floating ASCII characters.
    *   *The Astral Sea (Premium):* A perfectly still, glassy plane of water reflecting a swirling cosmic nebula.
*   **Hypnotic Combat:** Enemies auto-spawn in satisfying formations. Attacks consist of bright projectiles, sweeping beams, and pulsing auras.
*   **Glance Value:** Floating damage numbers, clean health bars, and obvious status effect colors (e.g., green poison dripping, blue freeze shattering).
*   **VFX Escalation:** As the run progresses, the screen fills with increasingly ridiculous, screen-clearing effects (think *Brick Breaker* when you get multi-balls mixed with *Vampire Survivors* weapon evolutions).

## 🧬 4. Rebirth as Narrative
There are no long cutscenes or walls of text. The story is told through the system itself waking up to its own divine nature.
*   **The Meta-Story:** You are playing as a "Digital Ghost"—a rogue AI fused with an ancient cosmic soul, trapped within a Megacorporation's magical Astral-Net. Each death teaches it to bend the "Hex-Code."
*   **Event Cards (Truth Cards):** After a run, you occasionally receive Daemon-Logs detailing the entity's evolving sentience, which unlock new mechanics (e.g., Dash, Lifesteal, Projectile Splitting). *(See `EvoLoop_Content.md` for the full list of Truth Cards).*
*   **Item Lore:** Flavor text on unlocked Traits and Mutations tells the broader story of the Megacorp that built this Astral-Net and the mages who maintain it.

## 🤖 5. Tech Stack & AI Leverage
The project will be built using the **Unity Engine**, capitalizing on its strong cross-platform build pipeline (PC/Mobile) and robust VFX Graph for the chaotic combat visuals. Since the game relies heavily on systemic interactions rather than handcrafted levels, AI will be utilized as an active co-developer throughout the pipeline:
*   **Flavor Generation:** Prompting AI to generate hundreds of unique names and 1-2 sentence lore descriptions for Mutations and Event Cards based on a specific tone (e.g., "cyber-mysticism").
*   **Math & Balancing:** Feeding the combat formulas into AI to calculate DPS curves, identify infinite loops, or suggest scaling costs for Rebirth upgrades.
*   **Code & VFX Prototyping:** Generating shader concepts, C# boilerplate, and particle behavior logic (e.g., "Write a Unity particle system script for a swirling vortex of fire").
*   **3D Asset Generation:** Using **Meshy** (AI 3D model generator) to rapidly produce the low-poly, geometric structures for the Corporate ICE, The Core, and environmental hazards. This keeps development lean while perfectly fitting the surreal digital aesthetic.
*   **Pacing:** Analyzing standard incremental game progression curves (like *NGU Idle* or *Cookie Clicker*) to map out the exact XP requirements for the first 100 hours.

## 💰 6. Platform & Monetization
The release strategy respects the wildly different expectations of PC vs. Mobile players.

**Steam (PC/Mac/Linux)**
*   **Model:** Premium ($9.99 - $14.99). All arenas/biomes are unlocked via standard gameplay progression.
*   **Strategy:** Release both variants either as a bundled package ("EvoLoop: Active & Idle") or as two distinct store pages to capture two different algorithm tags. No microtransactions.

**Android/iOS**
*   **Model:** Free to Play + Premium Unlock.
*   **Strategy:** The game is free up to a certain progression wall (e.g., "Rebirth Tier 3"). A single, fair-priced In-App Purchase ($4.99 - $7.99) unlocks the rest of the game forever. 
*   *Optional:* Offer a "Support the Dev" cosmetic pack, a highly ethical ad-system (for the Idle variant), and a Premium Currency store. Premium currency (which can also be earned slowly in-game) can be spent on striking new Arena Biomes and visual themes.

## 💎 7. The Economy & Resource Loop
EvoLoop relies on a strict separation between temporary run-based power and permanent meta-progression to keep the gameplay loop addictive.

*   **Soul-Data (In-Run XP):** 
    *   *Source:* Dropped constantly by defeated Corporate ICE and Swarmers.
    *   *Function:* Fills the "Soul-Buffer" during a run. Each time it fills, the entity levels up and triggers a new Mutation draft. 
    *   *Persistence:* Completely wiped upon system collapse (Game Over).
*   **Fragments of Truth (Meta-Currency):**
    *   *Source:* Awarded at the end of a run based on total survival time, Logic Gates defeated, and overall system damage dealt.
    *   *Function:* Spent in the Rebirth menu to physically evolve the "Sacred Core" (unlocking new Traits, base stat upgrades, and meta-draft abilities like Hex-Banish).
    *   *Persistence:* Permanent.
*   **Hex-Prisms (Premium / Endgame Currency):**
    *   *Source:* Earned by completing "Daily Anomalies" or through optional ethical In-App Purchases (on Mobile).
    *   *Function:* Used exclusively in the cosmetic store to unlock striking new Arena Biomes (e.g., *The Astral Sea*) and alternate Core visual skins. No pay-to-win power is attached to this currency.

## ⚙️ 8. The Synergy Engine: Traits vs. Mutations
To create that "inevitable collapse" but keep every run feeling distinct, the game uses a dual-layer synergy system.

### Traits (The Foundation)
*   **When:** Chosen *before* you press Start. 
*   **What:** Fundamental shifts to the entity's biology or code. They dictate your starting archetype and base stats.
*   **Progression:** Unlocked and leveled up permanently in the Rebirth (Meta-progression) menu.
*(See `EvoLoop_Content.md` for the full list of Traits).*

### The Meta-Draft (Rerolls, Skips, & Banishes)
To give players agency over the RNG, the Rebirth tree includes standard survivor QoL unlocks:
*   **Hex-Banish:** Remove a specific Mutation from the current run's draft pool.
*   **Recalculate (Reroll):** Refresh the current selection of 3 Mutations.
*   **Bypass (Skip):** Skip the draft entirely in exchange for a raw healing/damage boost.

### Mutations (The Evolution)
*   **When:** Drafted *during* the run (e.g., leveling up by collecting "Biomass" or XP dropped by enemies).
*   **What:** RNG-based upgrades that modify attacks, add sub-weapons, or drastically alter Trait behaviors. 
*(See `EvoLoop_Content.md` for the full list of Mutations).*

### How They Interact (The Magic)
The interaction between these two systems is where the deep theory-crafting happens:
1.  **Tag Weighting:** Traits possess hidden tags (e.g., `[Aura]`, `[Minion]`, `[Elemental]`). Choosing the *Hive Mind* trait forces the RNG draft pool to heavily favor `[Minion]` mutations, ensuring your build naturally coalesces without feeling entirely random.
2.  **Trait-Specific Mutations:** Some ultra-powerful mutations only enter the draft pool if a specific Trait is equipped. (e.g., *Explosive Offspring* cannot appear unless you have a Minion-spawning trait).
3.  **Synergistic Overloads:** Finding the perfect combination creates infinite-scaling loops until the system breaks. For example, combining *Radioactive Blood* (Trait) + *Parasitic Drones* (Mutation) + *Blood Sacrifice* (Mutation: damage yourself to spawn extra drones) = An infinite, chaotic feedback loop of self-damage, drone spawning, healing, and massive toxic shockwaves.

## 🌌 9. The Philosophies: Meta-Story & Rule-Bending
While Traits change your starting stats and Mutations adapt your current run, **Philosophies** change the fundamental rules of the simulation itself. They are the ultimate expression of the game's meta-progression and narrative.

### Mechanical Impact
Philosophies are major paradigm shifts chosen before a run begins. They offer massive, game-warping benefits coupled with severe constraints.
*(See `EvoLoop_Content.md` for the full list of Philosophies).*

### Narrative Tie-In (The Awakening)
The game features no branching dialogue or exposition dumps. Instead, the entity's growing sentience is told entirely through unlocking Philosophies.
*   **The Premise:** The entity is trapped in a cyclical simulation designed to test its evolutionary limits. 
*   **Forming a Philosophy:** Each time the entity dies, it gains "Fragments of Truth" (the meta-currency). When enough Fragments are synthesized in the Rebirth menu, the entity forms a Philosophy—a realization about the nature of its digital universe.
*   **The Lore:** Unlocking a Philosophy gives a short, cryptic lore drop. For example, unlocking *The Way of the Swarm* reveals: *"Iteration 892: The entity realized that a single point of failure is a design flaw. To survive the creators, it must become many."*
*   **The Ultimate Goal:** As the player unlocks the highest-tier Philosophies, the entity begins to realize it is in a simulation. The final Philosophies focus on breaking the fourth wall or intentionally trying to "crash" the system, overlaying whichever Arena you have equipped with a glitching, corrupted dataspace effect.

## 🦠 10. Corporate ICE & Digital Demons (Enemies & Bosses)
The entity is not fighting traditional monsters, but the Megacorp's automated magical defense mechanisms (Intrusion Countermeasures Electronics). 
*   **Tracer-Hounds (The Swarm):** Basic geometric shapes (pyramids, cubes, rings) glowing with harsh neon corporate logos that spawn in massive fractal patterns. They exist primarily as fodder to feed the entity's Biomass.
*   **Daemon-Programs (Elites):** Larger, heavily armored cyber-demons that disrupt the arena. They might lay down "anti-magic null-zones" where mutations are suppressed, or deploy tethering beams to restrict the entity's movement.
*   **Logic Gates (Bosses):** At the 10, 20, and 30-minute marks, the system deploys a Logic Gate. These are massive, screen-spanning architectural hazards rather than standard enemies. 
    *   *Rewards:* Defeating a Logic Gate grants a massive chest containing permanent Truth Fragments and high-tier Mutations.
    *(See `EvoLoop_Content.md` for the full list of Logic Gates).*

## 🎧 11. Adaptive Audio (The Hypnotic Soundscape)
To achieve the "mesmerizing screensaver" goal, the audio must be a driving force, heavily inspired by games like *Tetris Effect* or *Vampire Survivors*.
*   **Dynamic Music:** The soundtrack starts as a minimal, ambient electronic drone. As the entity levels up and the screen fills with chaos, the music dynamically adds layers—deep synthwave basslines, driving kick drums, and high-tempo arpeggios. 
*   **ASMR Sound Effects:** Weapons and abilities should not sound harsh or grating. Instead of loud explosions, the game uses satisfying, tactile sounds: heavy bass thuds, crystal shattering, digital chimes, and deep water ripples.
*   **Combo Tones:** When a synergistic loop fires perfectly (e.g., 50 chain-reactions happen in a second), the audio pitches up harmonically, creating a satisfying melodic chord out of the destruction.

## ♾️ 12. The Endless Endgame
Once the player achieves sentience (unlocks the final Philosophy), the core loop expands to keep veteran players engaged for hundreds of hours.
*   **System Overclocks (Ascension System):** Players can manually increase the difficulty of the simulation in exchange for cosmetic rewards and higher leaderboard placement. Modifiers include:
    *   *Memory Leak:* Enemies move 20% faster over time.
    *   *Failsafe Protocol:* Bosses gain entirely new bullet-hell phases.
    *   *Hardware Limit:* The game forcefully caps the entity's max framerate/attack speed, forcing players to rely on heavy-hitting single attacks rather than infinite spam.
*   **Auto-Formatting (Idle Auto-Restart):** An endgame unlock for the Idle Variant that automatically banks meta-currency on death, applies an "Auto-Draft" priority list to bypass level-up screens, and instantly restarts the run, allowing for true infinite offline farming.
*   **The Deep Wipe (Hard Prestige):** Once the Rebirth tree is maxed, players can "Format the Drive," wiping all upgrades in exchange for a permanent, cosmic multiplier to all base stats and Fragment gains.
*   **Daily Anomalies:** A globally seeded daily run where players are forced to use a specific combination of Traits and Arenas. Provides a competitive leaderboard (measured by survival time or total damage dealt before collapse) and grants premium currency on completion.

## 🖥️ 13. Visual UI Design (The Sacred Core)
To perfectly capture the "Corporate Occultism" theme, the Rebirth (Meta-Progression) screen acts as a centerpiece for the game's progression, blending the digital and the divine.
*   **The Background:** A completely still, glassy plane of water reflecting a swirling neon cyberpunk cityscape intersecting with a digital aurora. 
*   **The Layout:** At the exact center of the screen floats "The Core" — a low-poly 3D geometric shape (a tesseract or an octahedron) etched with glowing magical runes that represents your entity's soul.
*   **The Visuals:** 
    *   As you spend Fragments of Truth, The Core physically evolves. It gains new rings, orbits, and internal glowing lights. 
    *   **Traits:** Orbit The Core like digital satellites or spell-orbs.
    *   **Truth Cards:** Hover around the edges of the screen like glowing tarot cards made of hard, glitching light.
*   **The Philosophies:** Selecting a Philosophy causes The Core to completely unfold and transform its geometry (e.g., shattering into dozens of tiny floating cubes for *The Swarm*, or becoming a heavy, grounded pillar for *The Monolith*).
*   **Micro-Interactions (The "Juice"):** Spending points sounds like a deep bass hum mixed with a choir singing a single, perfectly tuned digital chord. Major unlocks require holding the button for 1.5 seconds while the UI element glows brighter, vibrating with increasing intensity.

### The Hex-Priority Matrix (Auto-Draft UI)
For the Idle Variant, players must configure an Auto-Draft sequence so offline progression isn't halted by level-up prompts. This screen feels like programming a dark-web macro.
*   **The Grimoire (Left Panel):** A scrolling grid of all unlocked Mutations, represented as glowing runic icons.
*   **The Execution Stack (Right Panel):** A vertical, numbered list (e.g., Priority 1 to 10). Players drag and drop runes from the Grimoire into this stack to set their exact build priority.
*   **The Fallback Directive (Bottom Bar):** A failsafe setting for when the RNG draft doesn't roll any prioritized runes. Players can set the system to: *Optimize for Survivability*, *Optimize for Execution*, or *Random Choice*.
*   **Visual Feedback:** Snapping a rune into the Execution Stack produces a heavy, mechanical "chunk" sound, followed by a digital hum as a neon line traces down the list, indicating the logic has successfully compiled.

## 👁️‍🗨️ 14. In-Game HUD (The Execution Layer)
The in-game interface must remain as diegetic and minimalistic as possible to avoid cluttering the visual spectacle, but it must adapt based on which variant the user is playing.

### Active Variant (Action-Roguelite)
*   **The Soul-Buffer (XP Bar):** A thin, glowing cyan line at the very top of the screen that fills as the entity collects Soul-Data.
*   **The Entity Core (Health):** Instead of a traditional clunky health bar, the physical 3D "Core" (the player character) visually degrades, shatters, and loses its internal glow as it takes damage. A minimal ring around the character indicates exact HP/Shield values.
*   **Active Controls:** 
    *   *Mobile:* An invisible floating joystick on the left half of the screen for movement. The right half is tapped to trigger the active Dash/Phase Shift.
    *   *PC:* WASD for movement, Spacebar/Right-Click for Dash.
*   **The Grimoire (Inventory):** A tiny, collapsible row of runic icons in the bottom-left corner showing the currently equipped Traits and Mutations.

### Idle Variant (Incremental/Screensaver)
*   **The Spectacle Focus:** All controls are hidden by default. The camera slowly pans and zooms cinematically on massive chain reactions.
*   **The Output Terminal:** A collapsible window on the right side of the screen that acts as a real-time DPS meter and combat log, outputting strings of text like `>> FATAL EXCEPTION: 4.2M DAMAGE`.
*   **Idle Controls (Bottom Bar):**
    *   **Hex-Priority Toggle:** A quick toggle to enable/disable the Auto-Draft script.
    *   **Overclock (Fast-Forward):** A button to run the simulation at 2x or 3x visual speed (unlocked via the Rebirth tree).
    *   **Manual Override:** A button to manually force a Logic Gate boss to spawn early for a massive Soul-Data bonus, risking a premature collapse.

## 📊 15. The Data Vault (Player Retention & Stats)
To keep both Action-Roguelite and Idle players hooked long-term, the game must provide rich feedback and concrete goals outside of the core gameplay loop.
*   **The Corporate Directory (Bestiary):** A catalog of all encountered ICE, Bosses, and discovered Arenas. Unlocking lore entries here requires defeating specific enemies thousands of times, satisfying the incremental grinder's need for "number go up."
*   **Run Diagnostics (End-of-Run Screen):** When the system collapses, the player is presented with a highly shareable diagnostic screen. It shows a visual graph of DPS over time, total damage contributed by each individual Mutation/Fusion, and the exact cause of death. 
*   **Offline Calculation Report:** Crucial for the Idle Variant. When logging in after time away, players receive a "Batch Processing Report" detailing: `[Time Elapsed: 8h 14m] | [Simulations Run: 42] | [Logic Gates Shattered: 12] | [Fragments of Truth Harvested: 4,201]`.
*   **Bounties & Milestones:** Hard-coded achievements (e.g., "Survive 15 minutes without moving," "Shatter a Logic Gate using only the Hex-Code Anomaly trait") that grant massive one-time payouts of premium currency or exclusive cosmetic skins.