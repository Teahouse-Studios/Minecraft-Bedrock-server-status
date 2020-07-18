from be import status
import asyncio
result = asyncio.run(status('example.com','19132'))
print(result)
