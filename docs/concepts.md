# Blockwelt-Explorer – Concepts

Visual cheat sheet for the worksheet. Milestones 1–2 are done; the roadmap at the end shows what comes next.

---

## 1. Coordinates

```
        y (up)
        │
        │
        └────── x
       ╱
      z
```

- Ground (grass) is at **y = -2**, so the first free layer is **y = -1**.
- `player_position()` returns floats; `as_int=True` gives whole block numbers.

---

## 2. `setBlocks` takes two corners, not sizes

```python
world.setBlocks(x1, y1, z1,   x2, y2, z2,   material)
#               └ corner A ┘   └ corner B ┘
```

Everything in the box between A and B is filled, **with both corners included**.

```
Want 3 blocks in x, starting at x = 12:

x:   11   12   13   14   15
          [■]  [■]  [■]
           A         B          A = 12,  B = 12 + 3 - 1 = 14
```

> **Rule:** `end = start + count - 1`

❌ Old code: `setBlocks(x, y, z, 3, -1, 0, …)` treated `3, -1, 0` as fixed world coordinates.
Standing at x = 40 gave a strip from 40 down to 3 (38 blocks).

✅ Milestone 1 (`nr_1.py`), seen from the side:

```
 y
 3   S
 2   S                 S = sand   (4 in y)
 1   S                 B = brick  (3 in x)
 0   S                 T = stone  (5 in z, goes "into" the screen)
-1   B  B  B
     ─────────── x
     T T T T T  → z
```

---

## 3. Class vs. object

A **class** is the blueprint, an **object** is one thing built from it.
Every object has its *own* attributes (`self.…`).

```mermaid
flowchart LR
    C["class Wall<br/>(blueprint)<br/>width=6, height=5<br/>material='default:stone'"]
    C -- "Wall(pos, world)" --> O1["wall<br/>rotated = False"]
    C -- "Wall(pos, world)" --> O2["rotated_wall<br/>rotated = True"]
    O1 -- "build()" --> B1["6×5 wall along x"]
    O2 -- "build()" --> B2["6×5 wall along z"]
```

---

## 4. Reading the UML class diagram

```
┌──────────────────────────────┐
│ Wall                         │  ← class name
├──────────────────────────────┤
│ + width: int = 6             │  ← attribute : type = default
│ # bw: BlockWorld             │
├──────────────────────────────┤
│ + Wall(pos, bw)              │  ← constructor  →  __init__(self, pos, bw)
│ + build(): void              │  ← method, returns nothing
└──────────────────────────────┘
```

| UML | Meaning | Python |
|---|---|---|
| `+` | public: anyone may use it | `self.width` |
| `#` | protected: class + subclasses | `self._bw` (one `_`) |
| `-` | private: only this class | `self.__bw` (two `__`) |
| `= 6` | default value | set in `__init__`, **not** a parameter |
| `Wall(pos, bw)` | constructor | `def __init__(self, pos, bw)` |
| `: void` | returns nothing | no `return` |

> Python doesn't *enforce* `_`/`__`, it's a convention (and `__` triggers name mangling → `obj._Wall__bw`).

---

## 5. `rotated`: turning 90° around the y-axis

Top view (looking down, y points at you), wall starting at `pos = P`:

```
rotated = False             rotated = True
(runs along x)              (runs along z)

z                           z
↑                           ↑   ■
│                           │   ■
│                           │   ■
│                           │   ■
│                           │   ■
│   P ■ ■ ■ ■ ■             │   P
└──────────────→ x          └──────────────→ x
```

```python
if self.rotated:   # x stays fixed, z grows
    setBlocks(x, y, z,   x,               top, z + width - 1, …)
else:              # z stays fixed, x grows
    setBlocks(x, y, z,   x + width - 1,   top, z,             …)
```

Both walls in `main.py` start at the same `pos`, so they form an **L-corner**.

---

## 6. What happens when you press B

```mermaid
sequenceDiagram
    actor You
    participant W as world : World
    participant F as b_key_pressed()
    participant A as wall : Wall
    participant R as rotated_wall : Wall
    You->>W: press B
    W->>F: build_key_pressed(world)
    F->>W: player_position(as_int=True)
    W-->>F: (x, y, z)
    F->>A: Wall(pos, world)  → __init__
    F->>A: build()
    A->>W: setBlocks(... along x ...)
    F->>R: Wall(pos, world)
    F->>R: rotated = True
    F->>R: build()
    R->>W: setBlocks(... along z ...)
```

---

## 7. Why only ONE `World()`

Every `World()` opens its **own window**. The old code made three:

```mermaid
flowchart TB
    subgraph old["❌ before"]
        I["import wall"] --> W1["world = World()  (wall.py)<br/>window 1"]
        M1["wall.wall(..., World())"] --> W2["window 2"]
        M2["world = World()  (main.py)"] --> W3["window 3 ← you play here"]
        W1 -. "wall drew here" .-> X["invisible to you"]
    end
    subgraph new["✅ now"]
        N["world = World()"] --> NW["one window"]
        N -- "passed in as bw" --> NWall["Wall(pos, world)<br/>self._bw = world"]
        NWall -- "build() draws into" --> NW
    end
```

> **Pattern: dependency injection.** The wall doesn't create its world, it gets it passed in (`bw`).
> That's why the diagram has `bw` in every class.

---

## 8. Roadmap: the full worksheet diagram

```mermaid
classDiagram
    class Wall {
        +int width = 6
        +int height = 5
        +tuple pos
        +bool rotated = False
        +str material_id = "default:stone"
        #BlockWorld bw
        +Wall(pos, bw)
        +build() void
    }
    class WallWithDoor {
        +str door_material_id = "air"
        +build() void
    }
    class WallWithWindow {
        +str window_material_id = "air"
        +build() void
    }
    class Roof {
        +int width = 6
        +int depth = 6
        +str roof_material_id = "default:brick"
        +tuple pos
        -BlockWorld bw
        +build() void
    }
    class House {
        +Wall wallFront
        +Wall wallLeft
        +Wall wallRight
        +Wall wallBack
        +Roof roof
        +tuple pos
        -BlockWorld bw
        +build() void
        +change_wall_material(new_material_id) void
    }
    class HouseTest {
        +setUp() void
        +test_change_wall_material() void
    }
    Wall <|-- WallWithDoor : M3 inherits
    Wall <|-- WallWithWindow : M3 inherits
    House o-- Wall : M5/6 has 4
    House o-- Roof : M5/6 has 1
    HouseTest ..> House : M7 uses
```

| Arrow | Name | Meaning | Milestone |
|---|---|---|---|
| `──▷` hollow triangle | **Inheritance** | "is a": a `WallWithDoor` *is a* `Wall` | 3 |
| `──◇` hollow diamond | **Aggregation** | "has a": the House *has* walls/roof (parts can exist alone) | 5, 6 |
| `──◆` filled diamond | **Composition** | "has a, owns it": parts die with the whole | 5 |
| `- - ->` dashed | **Dependency / use** | the test *uses* House | 7 |
| `+ # -` | **Visibility** | see section 4 | 4 |
