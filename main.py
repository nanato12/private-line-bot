import asyncio
import traceback
from typing import List, Optional

import settings
from akad.ttypes import Operation, OpType
from events.RECEIVE_MESSAGE import RECEIVE_MESSAGE
from line import LINE, OEPoll


async def execute(client: LINE, op: Operation) -> None:
    if op.type == OpType.RECEIVE_MESSAGE:
        RECEIVE_MESSAGE(client, op)


def login() -> LINE:
    try:
        client = LINE(settings.AUTH_TOKEN)
        client.log("Token login")
    except Exception as _:
        client = LINE(settings.EMAIL, settings.PASSWORD)
        client.log("Email login")
        client.log(f"auth_token: {client.authToken}")
    return client


def run(poll: OEPoll) -> None:
    while True:
        try:
            ops: Optional[List[Operation]] = poll.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    asyncio.get_event_loop().run_until_complete(
                        execute(poll.client, op)
                    )
                    poll.setRevision(op.revision)
        except Exception as e:
            traceback.print_tb(e.__traceback__)


if __name__ == "__main__":
    run(OEPoll(login()))
