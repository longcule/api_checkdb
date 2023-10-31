
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
import json
from fastapi import FastAPI
from tfidf import find_answer
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post('/v1/chat/completions')
async def get_chat_completions(messages: List[Dict[str, str]]):
    print("hallo")
    return "oke"

@app.post('/v1/check/database')
async def get_check_database(messages: list[dict]):
    for message in messages:
        content = message.get("content")
        print(content)
        if content:
            data = find_answer(content)
            if data:
                return JSONResponse(content=data)
        return JSONResponse(content="Không tìm thấy câu trả lời nào!!")


@app.get("/")
def Home():
    return "Hehehehhehe Longcule day"




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=9090)
    # , reload=True
    