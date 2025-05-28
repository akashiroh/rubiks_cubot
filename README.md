# Rubiks Cubot

A Rubik's Cube Solving Robot.

**Contributors**
- Andrew Holmes
- Dylan Scott Carroll
- Tarnivir Virk
- Jonathon Ly

## Examples

![Demo Animation](figures/rubiks.gif)
**Solving a Rubik's Cube with Regular Moves**

![Demo Animation](figures/constrained.gif)
**Solving a Rubik's Cube with the Constrained Moves of our Robot**

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
    WOG
    WWR
    GBY
BOR WYB RWY RBR
RRR YBW BOW GGG
GYB OGB WBO GYW
    YOO
    GYR
    OOY


KC Moves: 52 moves -> B U2 L B D B2 U2 D' R F' U2 L2 D F2 U D2 R2 U' L2 B2
Rubiks Moves: 62 moves -> B U U L B D B B U U Di R Fi U U L L D F F U D D R R Ui L L B B
Constrained Moves: 132 moves -> X D X D D Y X D Y X D Yi X D Xi D D Xi D D X X Di Y X D Yi X Di Y X D D Yi X D D X D Yi X D D X D X X D D Y X D D X Di X D D Y X D D
Robot Moves: 142 moves -> ['rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_cw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_cw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_ccw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_ccw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_ccw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_cw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_ccw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_cw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_ccw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_ccw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_cw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'extend_fork', 'rotate_fork_cw_90', 'retract_fork', 'rotate_tray_cw_90', 'lower_hand', 'rotate_fork_??_90', 'raise_hand', 'lower_hand', 'rotate_fork_??_90', 'raise_hand'] 
Success! In 62 moves | 35.63% solve moves as scramble moves
```

```
# Average from 100 simulations of random scrambles
Average scramble moves: 100 | Average Constrained Solve Moves: 61
```
