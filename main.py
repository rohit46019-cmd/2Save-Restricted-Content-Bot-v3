# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.

import asyncio
from shared_client import start_client
import importlib
import os
import sys

# Use Render's PERSISTENT WRITABLE DIRECTORY
SESSION_DIR = "/tmp/sessions"
os.makedirs(SESSION_DIR, exist_ok=True)  # Ensure session folder exists

session_path = f"{SESSION_DIR}/telethonbot.session"
journal_path = f"{SESSION_DIR}/telethonbot.session-journal"

# (Auto delete removed as requested)


async def load_and_run_plugins():
    await start_client()
    plugin_dir = "plugins"

    plugins = [
        f[:-3] for f in os.listdir(plugin_dir)
        if f.endswith(".py") and f != "__init__.py"
    ]

    print("FOUND PLUGINS:", plugins)

    for plugin in plugins:
        print("FOUND PLUGIN:", plugin)
        try:
            module = importlib.import_module(f"plugins.{plugin}")
            run_func_name = f"run_{plugin}_plugin"

            if hasattr(module, run_func_name):
                print(f"Running {plugin} plugin...")
                run_func = getattr(module, run_func_name)
                await run_func()
            else:
                print(f"❌ run function missing in {plugin}")

        except Exception as e:
            print(f"Error in plugin {plugin}: {e}")


async def main():
    await load_and_run_plugins()
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print("Starting clients ...")
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        try:
            loop.close()
        except Exception:
            pass


