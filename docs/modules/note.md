# Module note.py

```python
from bilibili_api import note
```

笔记相关操作

?> 注意，笔记分为私有笔记和公开笔记...公开笔记实质为专栏
?> 公有笔记不限数量，私有笔记每稿件只能写一篇

## const dict NoteType

笔记类型枚举

## class Video

笔记类，各种对笔记的操作都在里面

### Attributes

| name | type | description|
| ---- | ---- | ---------- |
| credential | Credential | 凭据 |

### Funcitions

#### def \_\_init\_\_()
| name | type | description|
| ---- | ---- | ---------- |
| type | str | 笔记类型 |
| oid | int | 稿件 id |
| oid_type | int | 稿件 id 类型 |
| note_id | int | 笔记 id |
| credential | Credential \| None, optional | Credential 类 |

---

#### def set_oid()

| name | type | description |
| ---- | ---- | ----------- |
| oid | int  | av 号。     |

设置 oid。

**Returns:** None

---

#### def set_note_id()

| name | type | description |
| ---- | ---- | ----------- |
| note_id | int  | note_id。 |

设置 note_id。

**Returns:** None

---

#### def set_cvid()

| name | type | description |
| ---- | ---- | ----------- |
| cvid | int  | cvid 专栏号。 |

设置 cvid。

**Returns:** None

---

#### def get_oid()

获取 oid。

**Returns:** str: oid

---

#### def get_cvid()

获取 cvid。

**Returns:** str: cvid

---

#### def get_note_id()

获取 note_id。

**Returns:** str: note_id

---

#### async def get_info()

获取笔记信息。

**Returns:** API 调用返回结果。

---

#### async def get_content()

获取笔记内容。

**Returns:** API 调用返回结果。

---

#### async def get_summary()

获取笔记摘要。

**Returns:** API 调用返回结果。

---

#### async def get_images_raw_info()

获取笔记所有图片原始信息。

**Returns:** API 调用返回结果。

---

#### async def get_images()

获取笔记所有图片并转为 Picture 类。

**Returns:** List[Picture]

---

#### async def get_title()

获取笔记标题。

**Returns:** str: 标题

---

#### async def get_author()

获取笔记作者信息。

**Returns:** dict: 作者信息

---

#### async def get_video()

获取笔记视频信息。

**Returns:** dict: 视频信息