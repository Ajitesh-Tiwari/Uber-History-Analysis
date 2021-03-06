from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path='/Users/atiwari4/Downloads/chromedriver', chrome_options=option)

browser.get("https://riders.uber.com/trips")
time.sleep(60)

arr = ["https://riders.uber.com/trips/7e51cd92-341e-4658-8159-c41ef3563c8e",
"https://riders.uber.com/trips/7aea5667-c16d-4701-93f4-bdd3292cff7a",
"https://riders.uber.com/trips/266dfca1-90d9-4a3c-a279-93e8f7f57aca",
"https://riders.uber.com/trips/7e8f26bc-df31-4991-8f27-3f5e9e5c282e",
"https://riders.uber.com/trips/7728ac56-5663-4b56-bd1a-446173ac7d39",
"https://riders.uber.com/trips/be10c43a-3a80-4c34-8565-65fcda2a76c4",
"https://riders.uber.com/trips/d0bf7ed2-f7c2-48ca-9f53-557c78344857",
"https://riders.uber.com/trips/aaa236e2-e109-4e8c-bfcf-d7bc03388310",
"https://riders.uber.com/trips/a806041f-b056-4fd6-8b76-7a91836fbb57",
"https://riders.uber.com/trips/532655cf-156c-4fb2-b002-bcd6ced89c2e",
"https://riders.uber.com/trips/18fbc880-1171-4a92-83d9-49709d8a0513",
"https://riders.uber.com/trips/1fc46f05-4025-47cc-9309-a1d368966baf",
"https://riders.uber.com/trips/4f3bf265-3168-48dd-8275-435e720b0bf1",
"https://riders.uber.com/trips/54932d54-4c0d-4b35-ad63-2afb290d25fc",
"https://riders.uber.com/trips/dafc8f68-8aed-4dcf-ac27-5a2dc54cb668",
"https://riders.uber.com/trips/6df4e857-0427-4bd9-8b7d-025baa8d178f",
"https://riders.uber.com/trips/29d6be99-1170-4f7d-873f-9a020ba095b1",
"https://riders.uber.com/trips/c6f38ecc-307e-40c6-bfc2-9549abcd3ef6",
"https://riders.uber.com/trips/7ffbb149-f832-449f-a22d-60c70cbef0af",
"https://riders.uber.com/trips/5d1ccfd7-f4db-486e-a233-dc0b45afcb83",
"https://riders.uber.com/trips/8965186b-060c-42b2-972b-e5f5f7b12cd9",
"https://riders.uber.com/trips/ed47cc87-ebb8-4ddb-aa39-46558aba4f6f",
"https://riders.uber.com/trips/e5a3ebe0-e1f1-4cab-bda1-f5f4a882be4b",
"https://riders.uber.com/trips/f6f044e8-c920-4830-aadb-299e8d13d6ca",
"https://riders.uber.com/trips/df299d12-6316-4f6c-88a2-95ffb8629d9a",
"https://riders.uber.com/trips/74c287ed-9ffb-46f1-8dad-b56b05678cbe",
"https://riders.uber.com/trips/03512f40-778b-4106-b699-851b6cde7ab1",
"https://riders.uber.com/trips/996697c0-e3fd-46a9-a067-b28a17aa3c7d",
"https://riders.uber.com/trips/8a5004ce-a96e-428a-9944-2a9ba25363ac",
"https://riders.uber.com/trips/1bde3de7-b37b-47f4-8161-5f4896ef504c",
"https://riders.uber.com/trips/011e8f76-61ae-4e2c-8593-e6d837f790da",
"https://riders.uber.com/trips/c0c8f72f-845f-4ab5-a25e-c921130cfe2f",
"https://riders.uber.com/trips/91202808-fc2b-4c2b-8949-fa9ed009755a",
"https://riders.uber.com/trips/2d8ec0ab-047f-4a1d-bd84-b364456d5983",
"https://riders.uber.com/trips/443ae497-1a05-4085-97c4-22a52a5330bd",
"https://riders.uber.com/trips/88a8f52b-1529-4e7b-ba00-ff936bb10304",
"https://riders.uber.com/trips/a17a3668-e8ab-495c-afab-bc2b80219888",
"https://riders.uber.com/trips/57fb0666-5a6d-4869-bdff-d7480ebc96be",
"https://riders.uber.com/trips/d9f7cd1e-b630-455a-9b02-f38e1c2f5eab",
"https://riders.uber.com/trips/cff1c32b-01b4-4655-81c0-719a8d8ee761",
"https://riders.uber.com/trips/abc02ef5-a815-40aa-974e-7aad41dc34a0",
"https://riders.uber.com/trips/3422086c-d4ea-4ccd-b4ac-0c9abd93b312",
"https://riders.uber.com/trips/6580eacf-504d-4039-a3da-cc77f79354c8",
"https://riders.uber.com/trips/6e40801f-45d4-4a80-9acc-f224f3d45ad6",
"https://riders.uber.com/trips/71f12d8a-d330-4bd1-bdfe-316f446f33b9",
"https://riders.uber.com/trips/a7c18eb8-a000-4c99-9d2e-52ec3491f2b9",
"https://riders.uber.com/trips/99926df8-aa3c-4260-ac14-96309f66d135",
"https://riders.uber.com/trips/5f721525-c7b4-48f5-89f2-d8a1901799f3",
"https://riders.uber.com/trips/a2dc7450-1b4c-4135-aebf-26674117babb",
"https://riders.uber.com/trips/3bf927f5-c2aa-4341-8fd2-369b7a78a085",
"https://riders.uber.com/trips/6e0eae92-4ed7-4f3f-967f-7439ba13b202",
"https://riders.uber.com/trips/c812b366-d4a2-4251-8c53-f8422b7c0cf3",
"https://riders.uber.com/trips/d10e747b-465c-445b-aca5-e60019b34ff3",
"https://riders.uber.com/trips/c70651a3-c386-49b6-82c2-ffa0d77e3d25",
"https://riders.uber.com/trips/d3354c94-7585-460f-a817-563d4ba3e733",
"https://riders.uber.com/trips/624406a1-f1fe-4b71-9263-88992380d62a",
"https://riders.uber.com/trips/537d14d7-5065-4e1f-a8b0-1f71ce53c3af",
"https://riders.uber.com/trips/c238d89a-ce39-44f1-b7bd-221faae0b75f",
"https://riders.uber.com/trips/d891a88d-6cfb-45b7-abd5-7af1ddfc5c4b",
"https://riders.uber.com/trips/06a5a0d4-d115-487c-b6fb-0852f4e90aa1",
"https://riders.uber.com/trips/0549c4e1-a1b2-4a1d-9421-45ce03c88e99",
"https://riders.uber.com/trips/8eb81528-9fa1-4bd1-b8be-00ba093c6eb7",
"https://riders.uber.com/trips/abfaf020-781f-46d4-9fb5-32e8f7bfee0c",
"https://riders.uber.com/trips/023c8c29-d0ee-4edd-b841-2c3cd5bc86c1",
"https://riders.uber.com/trips/550131b7-da43-4811-b9e1-504802157749",
"https://riders.uber.com/trips/1c9114c2-ea50-45e6-bbbd-188457afda2d",
"https://riders.uber.com/trips/384651dc-636f-4e3d-accf-6c5f072ee028",
"https://riders.uber.com/trips/889c31c1-5995-4be1-b345-21c8aa5ada5c",
"https://riders.uber.com/trips/7b86a212-8671-4031-923b-63f82ca97a51",
"https://riders.uber.com/trips/2210f8f4-6e8d-47b0-86d7-0bcfbed56ff1",
"https://riders.uber.com/trips/d1e95239-40a3-43e2-96cc-7412f7e30110",
"https://riders.uber.com/trips/6c8b0aef-77af-42e4-9ad2-3e1ae549138d",
"https://riders.uber.com/trips/d889a946-5f8e-4e7e-9386-b88ddbcc055e",
"https://riders.uber.com/trips/996b83b5-36d5-4b62-984f-466fa9afdc03",
"https://riders.uber.com/trips/84991278-3cf5-475c-9bc8-a8eb35457bd1",
"https://riders.uber.com/trips/b73329e3-f667-43b3-a10d-ce5c6e8735af",
"https://riders.uber.com/trips/0d9512cf-1b99-4444-8d6c-57dbb3b74701",
"https://riders.uber.com/trips/fdbd44e5-a14d-4e1f-818a-3ad519f2ae3b",
"https://riders.uber.com/trips/85ee9559-8d5f-4b17-87e3-6d433ae66fdb",
"https://riders.uber.com/trips/e398bcaf-5d68-42c7-8910-8a7fea5c43f0",
"https://riders.uber.com/trips/a810fafe-8917-4de0-b0a4-7bd6aba179e6",
"https://riders.uber.com/trips/9ddb3830-4d70-4bf7-8253-8d8aa04dddac",
"https://riders.uber.com/trips/47ddad8b-db9d-4e6f-a6ab-40f3ed976d50",
"https://riders.uber.com/trips/5f7032d6-96ca-4880-aa36-9175f26ba54d",
"https://riders.uber.com/trips/631ed661-b295-494b-80fb-76ecb1215c60",
"https://riders.uber.com/trips/90efe3f5-fe08-43f0-b7b3-1a1ca176bb48",
"https://riders.uber.com/trips/9641b1ff-5670-463b-8598-bd43c5e76dd4",
"https://riders.uber.com/trips/b47c4ad6-978a-4823-870e-865e677dbbb2",
"https://riders.uber.com/trips/65d3af58-9ad8-48e0-9a42-1dc4d9f6fdba",
"https://riders.uber.com/trips/9dbd1b97-93fe-429f-9b29-1cdcd4510f1a",
"https://riders.uber.com/trips/c5d68a75-1b5d-411b-9fb5-afe371f6ccaa",
"https://riders.uber.com/trips/60ba4c3c-18db-4409-a0a1-2da95d3c0ae2",
"https://riders.uber.com/trips/48472f20-e30d-4851-8512-202997b86dd9",
"https://riders.uber.com/trips/f979b3fe-f13a-4179-8d1d-e0f114501b0a",
"https://riders.uber.com/trips/046f58cf-3f01-445c-9195-388061b16e93",
"https://riders.uber.com/trips/1b773f1e-ca74-491b-8aca-189efb3f53cf",
"https://riders.uber.com/trips/fc351693-ef9f-496a-afaf-0ac0ff9871e7",
"https://riders.uber.com/trips/9c936285-a654-49b2-9aeb-583ede9f5715",
"https://riders.uber.com/trips/da0b19e9-eb96-4813-a189-7d73eb7d21a4",
"https://riders.uber.com/trips/5857f1c0-d74e-4c38-a9bf-9726b0b4c0cb",
"https://riders.uber.com/trips/f8456300-cc61-40bb-8a60-02dd2ad7998a",
"https://riders.uber.com/trips/710ffc41-8948-4aa1-817d-1ad453bed32a",
"https://riders.uber.com/trips/86eb0364-3e49-4785-8aef-9c6a910aeec9",
"https://riders.uber.com/trips/441d47f3-275b-4156-81a3-d3936e77edc6",
"https://riders.uber.com/trips/31418eea-dd4b-47a4-91ee-17ca043a7b8b",
"https://riders.uber.com/trips/0cccc8c8-f069-47f3-965e-e0deeee84de1",
"https://riders.uber.com/trips/e961d856-e394-45f7-b0dc-5235edbdb2ef",
"https://riders.uber.com/trips/5fbf7c9d-d99d-47f5-8f1e-f69318799e91",
"https://riders.uber.com/trips/17428e08-8c19-4e36-a8a7-c1c4c6745af8",
"https://riders.uber.com/trips/6d8af859-6a7d-4684-9b96-fbf02c06e5f7",
"https://riders.uber.com/trips/add23114-3e14-4b31-b737-b43ad413b0de",
"https://riders.uber.com/trips/cd23be9e-8b07-4ba1-8448-23de80e67f3b",
"https://riders.uber.com/trips/afac6a16-dcb9-4bc7-b1d4-2dd5fc92d8be",
"https://riders.uber.com/trips/4efe1274-8299-44d3-ac41-17e0f07de6a0",
"https://riders.uber.com/trips/ab772517-126d-4912-9768-8e782a6737db",
"https://riders.uber.com/trips/cdb9f4d4-d2c2-436c-978c-1bf115e2baa7",
"https://riders.uber.com/trips/1c8f39cb-5960-49d0-bba5-cf69a78fd668",
"https://riders.uber.com/trips/34d333f3-0bed-4be9-b258-07595f08f630",
"https://riders.uber.com/trips/0c1521d5-8184-40e6-88b4-39d2e1d4989d",
"https://riders.uber.com/trips/6c814746-5c6c-4f16-be7a-8709f4506696",
"https://riders.uber.com/trips/db24ebef-1442-44ff-9853-c20c5302f3f0",
"https://riders.uber.com/trips/7caf0f93-c042-457c-a3df-0b3d9cb3c2f7",
"https://riders.uber.com/trips/f8b5fdc1-9e46-4a79-9a59-19ecc02dad37",
"https://riders.uber.com/trips/665fe4c8-19c9-4fe3-b75c-f70bbf82b001",
"https://riders.uber.com/trips/1e80a688-633d-4719-a025-0004b5f3ea1f",
"https://riders.uber.com/trips/171269d7-9066-4b9c-b9e3-c91a627251db",
"https://riders.uber.com/trips/d0e96c71-9d3f-4994-9523-49fd993bfa47",
"https://riders.uber.com/trips/f74b8070-8ba9-4cd7-b7c8-51f5f37cbbe6",
"https://riders.uber.com/trips/39ea937d-73d7-47b6-97ca-6c26a9e01815",
"https://riders.uber.com/trips/1a22a11b-03dc-45df-b7c0-8816eb5cfd7f",
"https://riders.uber.com/trips/19ee05a2-7a62-420f-998a-5c38434e3e78",
"https://riders.uber.com/trips/f6ea26bf-2447-49ea-8eb2-336854b250ef",
"https://riders.uber.com/trips/2f18491c-5e86-4e05-a752-c388d63f8a6e",
"https://riders.uber.com/trips/ecb4bbb9-c0ba-44e2-9a76-ab7f82eea984",
"https://riders.uber.com/trips/74abbd2a-4fd4-45bc-b989-66d2d623151e",
"https://riders.uber.com/trips/066ec97b-13e4-4131-8155-ee689c344798",
"https://riders.uber.com/trips/11eaf8f2-ed77-403e-8abc-4df3a69f7bee",
"https://riders.uber.com/trips/632822cf-357a-4f67-94b2-9322e4ddaafb",
"https://riders.uber.com/trips/14474998-765e-46fe-a4e2-937c67b49417",
"https://riders.uber.com/trips/3d346b7a-fb4d-4035-856d-f8d08aa780fd",
"https://riders.uber.com/trips/2d936658-410b-44b4-bab8-4be17d34b0b4",
"https://riders.uber.com/trips/3c3df6f2-3f0a-4a82-b1b2-1c8061601cf3",
"https://riders.uber.com/trips/8541504f-261a-4692-8006-c3e09ab7d9bf",
"https://riders.uber.com/trips/5275c051-3899-4f60-80fe-2304ae9e6fd2",
"https://riders.uber.com/trips/50cd3d4b-48d5-4d3f-bf4a-6058f25358f4",
"https://riders.uber.com/trips/6a0034cf-f292-45fc-8c91-3095905f4e56",
"https://riders.uber.com/trips/db024fa7-c24f-40d4-a3e0-75cc99a5eed7",
"https://riders.uber.com/trips/f7d06b1b-1511-4793-a3a3-e2de8ce9f50d",
"https://riders.uber.com/trips/9ecbe7a4-3042-45a8-98d0-100c6e1968a2",
"https://riders.uber.com/trips/b4f4246f-f532-4198-86c0-1da0046098e3",
"https://riders.uber.com/trips/c641eb50-06fb-4585-aa1e-8f3954c166c7",
"https://riders.uber.com/trips/92c93efa-8c04-4db8-a18f-0305346b8006",
"https://riders.uber.com/trips/65f091cb-df8f-4518-92fa-95d2a5e6adc3",
"https://riders.uber.com/trips/7b286108-232c-4f0e-8b05-3de3c3583737",
"https://riders.uber.com/trips/f91d7eff-88a2-412d-b03a-4dcaf95186f5",
"https://riders.uber.com/trips/184ff80e-4873-4365-8059-f97d62400d06",
"https://riders.uber.com/trips/0a785513-6bdc-4fa1-995b-f3c217de04da",
"https://riders.uber.com/trips/e4617fea-732a-485a-97d8-f88730cab7b0",
"https://riders.uber.com/trips/02ff4c75-be16-497f-b997-229a75bd5078",
"https://riders.uber.com/trips/d5cd65c4-b92a-48ef-ae5d-f228acac1c32",
"https://riders.uber.com/trips/164dc3af-9b0c-4adf-a96b-935a3cb76f09",
"https://riders.uber.com/trips/5dbc1ccb-4967-4010-98b3-19291b2fd7af",
"https://riders.uber.com/trips/0e38e798-41b6-42a5-a214-3bdbe77e795f",
"https://riders.uber.com/trips/0efd3323-0dff-40ba-bad6-0857507832a9",
"https://riders.uber.com/trips/bc90f630-4587-48a8-bed4-6f8707a6f85d",
"https://riders.uber.com/trips/a78215d1-d79f-4c81-ae00-45d26e1da9fd",
"https://riders.uber.com/trips/7854bff9-fa10-4d3e-8aea-d5ba228ad792",
"https://riders.uber.com/trips/fa09b58f-b6c5-4527-877d-e85a71b970e2",
"https://riders.uber.com/trips/0375a967-2b4a-47f3-a59d-5cfb693e3f10",
"https://riders.uber.com/trips/978c3bab-be1a-4de8-bce7-3934e6ee0c27",
"https://riders.uber.com/trips/42d276ca-8071-4c24-9b04-4c163443dc37",
"https://riders.uber.com/trips/adce4026-e14a-406b-aab2-3a872bdaed85",
"https://riders.uber.com/trips/8cf50701-8805-4185-9787-7acfc263a8de",
"https://riders.uber.com/trips/509092d8-7c32-47c2-9eaa-51e23de508b4",
"https://riders.uber.com/trips/45f496de-64cb-48a2-8049-424907905e03",
"https://riders.uber.com/trips/c382e9d3-c381-4a3f-a40e-9903778a9807",
"https://riders.uber.com/trips/011874b4-f238-46ab-8151-66cc88a9ff0e",
"https://riders.uber.com/trips/0c392c85-35b6-44b1-b998-ef9c448a2989",
"https://riders.uber.com/trips/d773ab35-4fe3-48b7-9a90-d7ba559da637",
"https://riders.uber.com/trips/71aef05c-0dcf-4592-bc1e-ae7aceeb59e2",
"https://riders.uber.com/trips/653be036-a942-4cbd-a175-e1f8095c7cf3",
"https://riders.uber.com/trips/5117e1d6-f035-4609-a698-15efc3f42465",
"https://riders.uber.com/trips/a607ff05-46a0-4007-8621-2d59df85c4bf",
"https://riders.uber.com/trips/04655c67-b943-4f47-822b-57fefa404db0",
"https://riders.uber.com/trips/f5c048d2-e4d3-4226-8271-cb7d994b91eb",
"https://riders.uber.com/trips/c07928c0-e3fd-4d69-ae32-e8c895f8b3b7",
"https://riders.uber.com/trips/b5c6090f-8a8b-49fe-97e7-71938b9737c6",
"https://riders.uber.com/trips/58c307cd-bed7-4c64-85e7-dd28c00abc0c",
"https://riders.uber.com/trips/0bd15bbd-3ac0-46b1-b66d-544ae1c3716d",
"https://riders.uber.com/trips/a40aff69-16f6-4f17-8655-5fef2d662b8e",
"https://riders.uber.com/trips/e3d1ac4b-be78-4d73-9fd4-46ebed98164f",
"https://riders.uber.com/trips/9e1e7126-ca88-49de-b9b0-e58ba5480a31",
"https://riders.uber.com/trips/14712702-9cd6-408e-bacd-4b6c658c65c3",
"https://riders.uber.com/trips/1c8892a1-8887-493b-9063-09314fda352a",
"https://riders.uber.com/trips/58357ddd-7887-42d8-8fee-a063ecdecec2",
"https://riders.uber.com/trips/f91e8e9b-e7d3-4e0f-8757-e79799613c83",
"https://riders.uber.com/trips/77b6ef94-01c8-4cdd-a277-138ac4edb87d",
"https://riders.uber.com/trips/1f2f20f7-b3e4-4392-8e84-017e01e52118",
"https://riders.uber.com/trips/51f42d25-174c-4035-8c67-5c2a0c77f87b",
"https://riders.uber.com/trips/6d1ba9da-5c9b-4ff7-83b4-5dfb5ed1b770",
"https://riders.uber.com/trips/49d640b6-cd75-405c-b559-d04b2580e21f",
"https://riders.uber.com/trips/b3612a16-20d3-4ab7-9773-8f687989ac99",
"https://riders.uber.com/trips/cb65ce06-c656-49fd-88cc-a4fca0303a87",
"https://riders.uber.com/trips/691f5019-3c82-4ddd-8944-cd30742da29c",
"https://riders.uber.com/trips/77463266-3b48-4352-8d5c-5a72147aed4a",
"https://riders.uber.com/trips/889be998-41e6-4cf7-b0d0-bd2493e577c5",
"https://riders.uber.com/trips/63eee809-2df8-4f9e-94fc-a77bd99af3e1",
"https://riders.uber.com/trips/e21db70d-8265-44fd-ad93-962cb7e658ef",
"https://riders.uber.com/trips/13cc73ba-912f-447d-97c5-be5cf99de54d",
"https://riders.uber.com/trips/ee9905ca-754d-4647-ac4f-8faab27b9f2a",
"https://riders.uber.com/trips/09ccba59-436f-44ff-8519-01eb102cffbb",
"https://riders.uber.com/trips/3847ff7e-c44b-4284-8543-d953a52a65c7",
"https://riders.uber.com/trips/95718515-d6ad-49d0-98ac-da6ba7062730",
"https://riders.uber.com/trips/bb0594c5-f779-45fc-9925-42bace5aac18",
"https://riders.uber.com/trips/9b5f43f9-9288-488d-b6b5-b04ab0747275",
"https://riders.uber.com/trips/f017b6b9-5ba8-4e59-a2f7-7bfe04c0d941",
"https://riders.uber.com/trips/2e7bc8b9-1617-4648-b7a5-c30515f56bc9",
"https://riders.uber.com/trips/a247f2ef-31b3-406b-9c9b-2b7edcef8275",
"https://riders.uber.com/trips/816af9d8-3387-44eb-9a44-570bba92e38a",
"https://riders.uber.com/trips/b1969102-f861-4258-9367-7fbfe9200fc0",
"https://riders.uber.com/trips/428853c5-7d2a-4054-8826-1c483f71bbd0",
"https://riders.uber.com/trips/e81ef49b-6dde-4acc-b3c8-2d0355f89247",
"https://riders.uber.com/trips/84b48446-4ea2-4a81-ac7b-5b4e5a2f76fb",
"https://riders.uber.com/trips/261fff97-74d1-414b-a67a-82be8827de1f",
"https://riders.uber.com/trips/36ca087e-1dc2-401e-a7f3-fc1afe4cd74f",
"https://riders.uber.com/trips/dad9936f-3a8d-4eed-94a3-52952adff161",
"https://riders.uber.com/trips/d304d2a4-2e2f-4a49-b0a0-728b1cef981a",
"https://riders.uber.com/trips/299f8200-66a4-4417-8403-f1b9c669800d",
"https://riders.uber.com/trips/14d8a175-5554-41e3-8c58-1a3a18652420",
"https://riders.uber.com/trips/696f926a-a88e-43cd-8101-2bac88f4fad6",
"https://riders.uber.com/trips/08fd247b-f1e0-4e2d-9561-d578e7706a2b",
"https://riders.uber.com/trips/22caab69-947d-42e3-ab87-2ff2b9c13b76",
"https://riders.uber.com/trips/bf581839-3beb-4066-a8f9-e5f0ffd10e62",
"https://riders.uber.com/trips/e2b33bf2-78b6-47fc-bc34-6044b0c95e59",
"https://riders.uber.com/trips/878ada7a-d27a-4104-acaa-b7ed89d9e0f0",
"https://riders.uber.com/trips/648b51e7-df4a-4b91-98f4-49f82eac9d1a",
"https://riders.uber.com/trips/cad2b57a-2e78-4bb1-b7b5-9ba59a211598",
"https://riders.uber.com/trips/e8be1cd1-48d4-4765-84f5-450f4912cad2",
"https://riders.uber.com/trips/243087ff-7e1e-4fc7-a5a9-f523604102ad",
"https://riders.uber.com/trips/1d1378a9-10d2-4e24-b257-74ca27109ef6",
"https://riders.uber.com/trips/42625886-410b-45f7-b049-ed1c587767c0",
"https://riders.uber.com/trips/1331417b-908d-4223-994f-b999dc9ff541",
"https://riders.uber.com/trips/476f50aa-ed7e-448c-af66-9f9ce0208c89",
"https://riders.uber.com/trips/ead19591-c5a9-475d-a8bb-24a6d24deb0c",
"https://riders.uber.com/trips/13b62fce-c86b-4d13-973f-5f2b30a45262",
"https://riders.uber.com/trips/5ca4d52d-2b88-41c5-a6de-48ad31028c5d",
"https://riders.uber.com/trips/2dc6b00c-bef2-449d-aaf3-e9a119132dbc",
"https://riders.uber.com/trips/fa90731b-a21a-473f-9482-a42494e7235e",
"https://riders.uber.com/trips/925059c0-8274-42e3-abb2-5affdb7946ef",
"https://riders.uber.com/trips/a3991395-0eb8-4e5b-8318-26a374810378",
"https://riders.uber.com/trips/37445df1-83d4-4991-9b5c-dd13f36effb2",
"https://riders.uber.com/trips/9b2d18ae-c9cc-4a8d-85cc-3e5eb827bc0a",
"https://riders.uber.com/trips/f7b0598e-0624-4a67-afa6-e089b351dbe8",
"https://riders.uber.com/trips/ae643fbd-6022-431b-8576-cf550012d1ef",
"https://riders.uber.com/trips/309d0e24-18e1-4794-83ab-83a6b5076987",
"https://riders.uber.com/trips/ce8f80e3-37ec-43d2-b99b-906fc67553b3",
"https://riders.uber.com/trips/9f5d41b7-3dce-4b89-bb77-f9ccbb13e30d",
"https://riders.uber.com/trips/63310cf0-e9e3-4004-ada6-6f77f6e61a72",
"https://riders.uber.com/trips/90db8409-8f1c-4b7d-a7be-4bfbaa44fda2",
"https://riders.uber.com/trips/3efcd0f4-6e76-48e0-b479-88ff08d5a9d3",
"https://riders.uber.com/trips/4e9ba84b-910f-4a41-ba65-d83786c488ff",
"https://riders.uber.com/trips/7ca2b8e2-f79a-4656-923f-8359984d2e65",
"https://riders.uber.com/trips/617c47d0-34ce-4f00-983d-6a0775ef43ca",
"https://riders.uber.com/trips/30f4cd75-66ec-4ee6-8633-a0aa106dbbf0",
"https://riders.uber.com/trips/9a56defe-f050-45da-8a23-b4241c6b4129",
"https://riders.uber.com/trips/5dcaac75-aecd-4809-b642-61772c3ca056",
"https://riders.uber.com/trips/bfdc1046-25bd-4c49-99fc-9ef93f8d5e50",
"https://riders.uber.com/trips/10794c9b-584b-4c51-9733-86ab6fc32177",
"https://riders.uber.com/trips/2a5d8c4e-c66f-4c5f-84ac-d38a57b731f5",
"https://riders.uber.com/trips/cf1e3848-b5a6-4cf9-9249-5d2346e9aa1d",
"https://riders.uber.com/trips/08329ff5-8bd4-4981-b041-9645bb6a5ad0",
"https://riders.uber.com/trips/ed5db4a3-b5a2-4066-9325-2ddfb9f63da3",
"https://riders.uber.com/trips/691e5509-c4c4-4a57-8b45-d3d302e53c4a",
"https://riders.uber.com/trips/e215c189-32b4-4f0e-a881-7df128c3a25d",
"https://riders.uber.com/trips/0017e783-ba23-4007-8354-588bd61b8fbc",
"https://riders.uber.com/trips/f422c6b4-a676-473d-8266-0f32c03925a3",
"https://riders.uber.com/trips/7014e6cc-a38f-44c9-bd89-8ccf177dc93d",
"https://riders.uber.com/trips/6c34c20f-c38b-47db-8228-bb6c341e2213",
"https://riders.uber.com/trips/b9d1c215-dd82-483a-bf2a-a96cf4395370",
"https://riders.uber.com/trips/20af035c-ba60-43f9-b94a-9f2de64ebf3c",
"https://riders.uber.com/trips/e67d6502-4f0f-47a8-ac7e-33adee221c9e",
"https://riders.uber.com/trips/329b5956-dc0e-4ba4-87af-fa874ffd0154",
"https://riders.uber.com/trips/c6c8b0a0-c4a2-45c4-8b0f-1a80ee8f2a47",
"https://riders.uber.com/trips/609d78eb-028a-4f30-b337-ee4510cebce3",
"https://riders.uber.com/trips/b120603a-0b53-4034-b451-75a3ec8bfff0",
"https://riders.uber.com/trips/990cc938-32c8-46dd-924b-9ddbdc21e88c",
"https://riders.uber.com/trips/7d21fd35-c915-4577-a3be-a88674d94f09",
"https://riders.uber.com/trips/6f964a8b-2528-4738-a3c0-b1cc4fc19507",
"https://riders.uber.com/trips/f16f185f-ae34-404b-a9d6-1712fd666274",
"https://riders.uber.com/trips/ff8217da-0ef7-4884-88da-6cac252d9ba6",
"https://riders.uber.com/trips/cc0616bf-1261-4a3e-8660-98bdd2d1117e",
"https://riders.uber.com/trips/8ae2415c-8012-4154-960e-79419095e694",
"https://riders.uber.com/trips/d78fb850-1937-41ef-8a96-e99aa32b1fa9",
"https://riders.uber.com/trips/9df1c7ec-262f-4718-92d2-d3b8af6010f0",
"https://riders.uber.com/trips/8db0c802-af07-4017-84d6-2c89881204c6",
"https://riders.uber.com/trips/352e7adf-e18d-4dab-8ea3-fdbc2ca17eb2",
"https://riders.uber.com/trips/2c51d84e-0ba2-4e9e-819c-79456c801ee6",
"https://riders.uber.com/trips/094ae17a-2020-40f1-a316-30d0895137f1",
"https://riders.uber.com/trips/c8e168ea-1cf1-4407-beff-57caf00c5f7f",
"https://riders.uber.com/trips/016432e8-9588-4917-a131-5268e02fae11",
"https://riders.uber.com/trips/8d8e5b2d-5b2e-44e6-bd43-c9c5abf2425a",
"https://riders.uber.com/trips/9415ac4b-9896-4524-8450-5fe2fd369d33",
"https://riders.uber.com/trips/b532498f-db78-4247-bc8a-9edf63cfebf8",
"https://riders.uber.com/trips/61db0842-a326-4980-8160-d71ee9828f50",
"https://riders.uber.com/trips/489c3f71-2515-4cdc-9594-8ecb19dfdaca",
"https://riders.uber.com/trips/78252949-7368-4cd9-9cc8-f7531ccbad2a",
"https://riders.uber.com/trips/4ce6f6d2-670c-4ada-99db-03bb340b3774",
"https://riders.uber.com/trips/cdc6186e-dd28-402f-8982-611ccd37b9c6",
"https://riders.uber.com/trips/a2a008ce-c839-49ed-bf71-7f99240024b9",
"https://riders.uber.com/trips/5ced45c4-9169-4395-84be-31f67145bb01",
"https://riders.uber.com/trips/eac62db4-17d5-4a2d-af7e-06f8bb8308f1",
"https://riders.uber.com/trips/e3937172-6503-4310-a53f-8b44b1505838",
"https://riders.uber.com/trips/57aa8e8a-334f-497a-a7a7-856d865e735c",
"https://riders.uber.com/trips/b27b3a35-ed3e-4a71-bca4-8093db0ee42c",
"https://riders.uber.com/trips/29639d84-14ae-4a89-893a-2a29fd63fc0b",
"https://riders.uber.com/trips/d28ab0df-2615-4dc0-bf3e-54dab95ab981",
"https://riders.uber.com/trips/42ed13d2-9f37-44e4-8d86-56ead04e4a3c",
"https://riders.uber.com/trips/a15aeb3f-ca04-4a23-bac9-ef6c3dba4a83",
"https://riders.uber.com/trips/0b17f68b-b371-4cb8-8503-39ef961d146a",
"https://riders.uber.com/trips/f814b88d-b1ca-45df-a1c6-faff603ad9fb",
"https://riders.uber.com/trips/77cc3116-a4cd-44d2-80a7-6e7c664331de",
"https://riders.uber.com/trips/0bf3931c-7cea-408e-a789-80a176fd2471",
"https://riders.uber.com/trips/e5a2c5e9-d0d3-48ca-bfb3-23d5f856e472",
"https://riders.uber.com/trips/15910d12-41b1-47a0-8ccd-3d66f44f0d71"]


for a in arr:
    row = []
    browser.get(a)
    time.sleep(3)
    distance = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/h5")
    trip_time = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div[3]/h5")
    row.append(a)
    distancex = [x.text for x in distance]
    row.append(distancex)
    trip_timex = [x.text for x in trip_time]
    row.append(trip_timex)
    print row
