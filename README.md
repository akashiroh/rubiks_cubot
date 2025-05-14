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

    RBY
    RWR
    WOW
GGO GGB OBO BWW
WRY OBY ROB OGG
BYR YRY OYW BWR
    GWG
    BYG
    YOR

Moves to solve:
    U R R B R Ui R R D F F L Fi L Bi L L D D B B R R Ui F F B B R R B B L L

Solved Cube.

    WWW
    WWW
    WWW
RRR BBB OOO GGG
RRR BBB OOO GGG
RRR BBB OOO GGG
    YYY
    YYY
    YYY
```
