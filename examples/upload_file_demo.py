# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/5/11 14:03

from typing import List

from pydantic import BaseModel, Field

from flask_openapi3 import OpenAPI, FileStorage, ExtraRequestBody
from flask_openapi3 import Encoding

app = OpenAPI(__name__)


class UploadFileForm(BaseModel):
    file: FileStorage
    file_type: str = Field(None, description="File Type")


class UploadFilesForm(BaseModel):
    files: List[FileStorage]
    str_list: List[str]
    int_list: List[int]


extra_form = ExtraRequestBody(
    description="This is form RequestBody",
    required=True,
    # replace style (default to form)
    encoding={"str_list": Encoding(style="simple")}
)


@app.post('/upload/file')
def upload_file(form: UploadFileForm):
    print(form.file.filename)
    print(form.file_type)
    form.file.save('test.jpg')
    return {"code": 0, "message": "ok"}


@app.post('/upload/files', extra_form=extra_form)
def upload_files(form: UploadFilesForm):
    print(form.files)
    print(form.str_list)
    print(form.int_list)
    return {"code": 0, "message": "ok"}


if __name__ == '__main__':
    app.run(debug=True)
