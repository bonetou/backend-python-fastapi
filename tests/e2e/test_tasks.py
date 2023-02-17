from src.dtos import CreateTaskDto


def create_task_dto_test():
    return CreateTaskDto(
        title="Foo",
        description="Bar",
        tags=["tag1", "tag2"],
    )


def test_should_create_task_correctly(test_client):
    create_task_dto = create_task_dto_test()
    response = test_client.post("/tasks", json=create_task_dto.dict())
    created_task = response.json()

    assert response.status_code == 200
    assert created_task["id"] == "1"
    assert created_task["title"] == create_task_dto.title
    assert created_task["description"] == create_task_dto.description
    assert created_task["tags"] == create_task_dto.tags
    assert created_task["completed"] is False


def test_should_not_create_task_with_blank_title(test_client):
    create_task_dto = create_task_dto_test()
    create_task_dto.title = ""
    response = test_client.post("/tasks", json=create_task_dto.dict())
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "title must not be blank",
                "type": "value_error",
            }
        ]
    }


def test_should_get_task_by_id_correctly(test_client):
    create_task_dto = create_task_dto_test()
    created_response = test_client.post("/tasks", json=create_task_dto.dict())
    created_task = created_response.json()

    response = test_client.get(f"/tasks/{created_task['id']}")
    assert response.status_code == 200
    assert response.json() == created_task


def test_should_return_not_found_error_if_task_does_not_exist(test_client):
    response = test_client.get("/tasks/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
