from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ddddocr
from pydantic import BaseModel
import uvicorn

ocr = ddddocr.DdddOcr(ocr=True, show_ad=False)

app = FastAPI()


class ocrItem(BaseModel):
    data: str  # 图片的base64编码


@app.post("/ocr")
def process_data(item: ocrItem):
    # res里是直接的识别结果
    res = ocr.classification(item.data)

    # {"result": "iepv"}
    return {"result": res}


if __name__ == "__main__":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 允许所有跨域
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)
