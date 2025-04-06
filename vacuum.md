# 📖 Study Guide: Vacuum Techniques & Plasma Technologies

## 1) Vacuum Equipment & Low-Pressure Measurement

### Vacuum Pumps

| **Type** | **Principle** | **Use Case** |
|----------|--------------|-------------|
| **Rotary (Oil-sealed)** | Mechanical piston compresses gas, expels at atmosphere | Rough vacuum (down to ~1 Pa) |
| **Roots blower** | Two rotors trap and move gas | Booster between stages |
| **Turbomolecular** | Rotor blades impact gas molecules axially | High to ultra-high vacuum |
| **Diffusion pump** | Oil vapor jet drags gas molecules down | High vacuum (down to ~10⁻⁷ Pa) |
| **Cryopump** | Condensation of gases at cryogenic surfaces | Ultra-high vacuum, clean, no oil |
| **Sorption pump** | Adsorption on cooled or activated surfaces (e.g., charcoal) | Clean vacuum, simple, no moving parts |
| **Ion pump** | Gas ionized, ions accelerated to cathode, trapped | Ultra-high vacuum (~10⁻⁹ Pa), no moving parts |

> Notes:
> - Lower pressure stages always need clean, high-speed backing pump.
> - Diffusion pumps need cold traps to avoid oil backstreaming.
> - Combination of pumps is standard for wide pressure range.

### Vacuum Gauges

| **Type** | **Principle** | **Pressure Range** |
|----------|--------------|-------------------|
| **Mechanical / Absolute** | Liquid column or diaphragm deformation | Atmospheric to 10² Pa |
| **Thermal (Pirani)** | Heat loss from filament to gas | 10⁵ to 10⁻³ Pa |
| **Thermocouple** | Measures temp of heated wire, changes with gas pressure | Similar to Pirani |
| **Ionization (Penning)** | Cold cathode ionizes gas, measures ion current | 10⁻² to 10⁻⁹ Pa |
| **Ionization (Triode)** | Hot cathode ionization, higher sensitivity | Ultra-high vacuum |

> Important:
> - No universal gauge covers all ranges.
> - Always combine types for safe operation.

---

## 2) Non-Equilibrium Plasma & Applications

### Generation of Non-Equilibrium Plasma

- **Electrical discharges**: DC, RF, microwave.
- **Pulsed plasma**: Short, high-energy pulses increase ionization.
- **Low-pressure environment**: Reduces collisions, keeps electrons "hot" while ions remain "cold".

> **Non-equilibrium plasma** = electrons have much higher temperature than ions and neutrals.

### Applications

- **Surface treatment**: Cleaning, activation, etching.
- **Deposition**: PECVD, sputtering.
- **Sterilization**: Medical tools.
- **Lighting**: Fluorescent lamps, plasma displays.
- **Propulsion**: Ion drives in space.

### Ion Sources

| **Type** | **Description** | **Use** |
|----------|----------------|----------|
| **Thermionic** | Heated filament emits electrons, ionizes gas | Basic plasma gen. |
| **Electron cyclotron resonance (ECR)** | RF power + magnetic field traps electrons | High-density plasma |
| **RF Ion Source** | Uses RF electric fields for ionization | Compact, versatile |

### Ion Drives for Satellites

- Accelerate ions (typically Xenon) via electrostatic fields.
- High exhaust velocity (~30 km/s), very efficient (Isp ~ 2000–10000 s).
- Require onboard neutralizer to prevent spacecraft charging.

> **Key**: Ion drives provide *continuous low thrust* for long missions.

---

## 3) Gas Laws, Kinetic Theory, Flows, Surface Processes

### Ideal Gas Laws

- **Boyle-Mariotte:** `pV = const` (isothermal)
- **Gay-Lussac:** `V ∝ T` (isobaric)
- **General:** `pV = nRT`
  - `R = 8.314 J/mol·K`

### Kinetic Theory

- Gas = moving particles; collisions produce pressure.
- `p = (1/3) n m v²`
- Maxwell distribution: speed of molecules spreads around an average.

### Types of Gas Flow

| **Flow Type** | **When** | **Description** |
|--------------|----------|-----------------|
| **Viscous / Hydrodynamic** | High p | Molecules collide with each other. |
| **Transitional** | Medium p | Mixed regime. |
| **Molecular flow** | Low p (~below 10⁻¹ Pa) | Molecules collide with chamber walls, not with each other. |
| **Effusion** | Tiny orifice, mean free path > hole size | Gas leaks through hole. |

### Surface Processes

- **Adsorption**: Gas sticks to surface.
- **Desorption**: Gas leaves surface (thermal or photon-induced).
- **Sputtering**: Surface atoms ejected by ion bombardment.
- **Monolayer formation time**:
  - `t = (3.2 × 10⁻⁴) / p` (p in Pa)

### Saturated Vapor Pressure

- Vapor in equilibrium with its liquid or solid.
- **Depends strongly on temperature**.
- Important for **contamination control** and **pumping limits** in vacuum systems.

---

## Strategy for Finals

- 🧠 **Visualize flows** (pumping stages, flow types).
- 🧩 **Draw pump + gauge chain** for typical setups.
- 🔥 **Drill plasma generation** and how ion thrusters work.
- ⚡ **Memorize flow transitions by pressure range.**
- ⏱️ **Estimate monolayer formation time** for contamination control.

---

**Optional Add-ons:**
- 🔥 Short cheat sheet PDF for printing.
- 📊 Flashcards (Anki-compatible).
- 🧩 Diagram(s) for visual brain-mapping.
