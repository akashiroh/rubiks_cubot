# Rubiks Cubot

A Rubik's Cube solving robot.

**Contributors**
- Andrew Holmes
- Dylan Scott Carroll
- Tarnivir Virk
- Jonathon Ly

## Environment Set Up

**Set up with UV**

- Install `uv`:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

- Create your environment by syncing with the provided files
   ```bash
    uv sync
    ```
    - To save the cache files to a different directory than the default /home
       ```bash
        uv sync --cache-dir /path/to/.cache/uv/
        
        or

        uv sync --no-cache
        ```

- Running a script with `uv`:
    ```bash
    uv run script.py
    ```

## Example

```
Scrambled Cube.
    YOG
    YWY
    RWB
RBB WGY ORY RGB
GRY OBW BOG YGR
OBW RRB WBG OWY
    GWO
    OYR
    GOW


Moves:                   Ri D F Di L Fi B Ui F B B Li Di R R Di B B R R D R R Ui R R F F
Constrained Moves:       Yi X Di Xi D Yi X D Xi Di Yi X D Y X Di X X D Yi X Di X D X X D D Y X Di Y X Di X D D Xi Di Y X D D Yi X D D Yi X D Xi D D Xi Di X D D Y X D D

Success! In 62 moves. 96.88%
Solved Cube.
    GGG
    GGG
    GGG
WWW OOO YYY RRR
WWW OOO YYY RRR
WWW OOO YYY RRR
    BBB
    BBB
    BBB

Average scramble moves: 64       Average Constrained Solve Moves: 62
```
