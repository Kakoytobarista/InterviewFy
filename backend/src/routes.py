from fastapi import APIRouter

from backend.src.interview.controllers import (task_controller, interview_controller,
                                               user_controller, interview_status_controller, interview_process_controller)


def get_apps_router():
    router = APIRouter()
    router.include_router(task_controller.router)
    router.include_router(interview_controller.router)
    router.include_router(user_controller.router)
    router.include_router(interview_status_controller.router)
    router.include_router(interview_process_controller.router)
    return router
