import asyncio
from datetime import timedelta

from opensandbox import Sandbox
from code_interpreter import CodeInterpreter, SupportedLanguage
from opensandbox.models import WriteEntry

async def main() -> None:
    # Create a sandbox with code interpreter
    sandbox = await Sandbox.create(
        "opensandbox/code-interpreter:v1.1.0",
        entrypoint=["/opt/code-interpreter/code-interpreter.sh"],
        env={"PYTHON_VERSION": "3.11"},
        timeout=timedelta(minutes=10),
    )

    async with sandbox:
        # Execute a shell command
        # execution = await sandbox.commands.run("echo 'Hello OpenSandbox!'")
        # print(execution.logs.stdout[0].text)

        # Write and read a file
        # await sandbox.files.write_files([
        #     WriteEntry(path="/tmp/hello.txt", data="Hello World", mode=644)
        # ])
        # content = await sandbox.files.read_file("/tmp/hello.txt")
        # print(f"Content: {content}")

        # Run code via the Code Interpreter
        interpreter = await CodeInterpreter.create(sandbox)
        result = await interpreter.codes.run(
            "import sys; print(sys.version); 2 + 2",
            language=SupportedLanguage.PYTHON,
        )
        print(result.result[0].text)  # 4

        await sandbox.kill()

if __name__ == "__main__":
    asyncio.run(main())
