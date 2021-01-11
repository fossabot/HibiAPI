from fastapi import APIRouter
from utils.exceptions import ExceptionReturn

from .bilibili import router as BilibiliRouter
from .netease import router as NeteaseRouter
from .pixiv import router as PixivRouter
from .qrcode import router as QRCodeRouter

router = APIRouter(
    responses={
        code: {
            "model": ExceptionReturn,
        }
        for code in (400, 422, 500, 502)
    }
)
router.include_router(PixivRouter, prefix="/pixiv")
router.include_router(BilibiliRouter, prefix="/bilibili")
router.include_router(QRCodeRouter, prefix="/qrcode")
router.include_router(NeteaseRouter, prefix="/netease")