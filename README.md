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
