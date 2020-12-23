pipelines = [{'name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf', 'item': {'models': [
    {'id': '37', 'names': ['document-structure-extraction-v2'], 'merge': {
        'parameters': {'query_value_ids': [], 'query_method': 'REGEXP', 'query_scopes': [],
                       'output_obj_type': 'PARAGRAPHS', 'query_value': '^(samsung|apple|huawei|xiaomi|vivo)',
                       'output_options': {'rows': [''], 'columns': ['']}, 'multi_match': True,
                       'output_content_type': 'PARAGRAPHS'}}}], 'created_date_time': '23-12-2020 11:06:49',
    'created_ts': 1608721609328,
    'metadata': {
        'display_name': 'updatetest1',
        'version': '1.0',
        'original_name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf'}}},
             {'name': 'pipeline-59f2bc60-6c2d-4520-a04c-71ad78e218e3', 'item': {'models': [
                 {'id': '37', 'names': ['document-structure-extraction-v2'], 'merge': {
                     'parameters': {'query_value_ids': [], 'query_method': 'REGEXP', 'query_scopes': [],
                                    'output_obj_type': 'PARAGRAPHS',
                                    'query_value': '^(samsung|apple|huawei|xiaomi|vivo)',
                                    'output_options': {'rows': [''], 'columns': ['']}, 'multi_match': True,
                                    'output_content_type': 'PARAGRAPHS'}}},
                 {'id': '42', 'names': ['document-structure-extraction-v2'], 'merge': {}}],
                 'created_date_time': '23-12-2020 11:07:00',
                 'created_ts': 1608721620077,
                 'metadata': {
                     'display_name': 'updatetest1',
                     'version': '2.0',
                     'original_name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf'}}},
             {'name': 'pipeline-27ea5494-7209-4e6b-9cb6-97ec5f4c7b98', 'item': {'models': [
                 {'id': '37', 'names': ['document-structure-extraction-v2'], 'merge': {
                     'parameters': {'query_value_ids': [], 'query_method': 'REGEXP', 'query_scopes': [],
                                    'output_obj_type': 'PARAGRAPHS',
                                    'query_value': '^(samsung|apple|huawei|xiaomi|vivo)',
                                    'output_options': {'rows': [''], 'columns': ['']}, 'multi_match': True,
                                    'output_content_type': 'PARAGRAPHS'}}},
                 {'id': '42', 'names': ['document-structure-extraction-v2'], 'merge': {}}],
                 'created_date_time': '23-12-2020 12:29:40',
                 'created_ts': 1608726580390,
                 'metadata': {
                     'display_name': '111111111',
                     'version': '3.0',
                     'original_name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf'}}}]

"""
// 创建多个技能
const batchCreatePipelines = async (url, ns, payloads = []) => {
  console.log(JSON.stringify(payloads));
  let rets = await Promise.all(
    payloads.map(({ name, item }, idx) => {
      return new Promise((resolve, reject) => {
        setTimeout(async () => {
          console.log(`${url}pipeline/${ns}/${name}`);
          let ret = await createPipeline(url, ns, name, item);
          resolve(ret);
        }, 0 + idx * 1500);
      });
    })
  );
  return rets;
};
"""

"""
// 更新一个组件，先删除后创建，会同步删除并重新创建组件相关的技能 （删技能-删组件-创建组件-创建技能）
const updateImg = async (url, ns, name, payload) => {
  let backup = await deleteImgAndRelatedPipelines(url, ns, name);
  console.log(
    `delete pipelines`,
    backup.map((b) => b.name)
  );
  let ret = await createImg(url, ns, name, payload);
  await new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(true);
    }, 1000);
  });
  let new_ppls = await batchCreatePipelines(url, ns, backup);
  return new_ppls;
};
"""


# for i in pipelines:
#     print(i)
#     pipeline = i['name']
#     print(pipeline)
#     payload = i['item']
#
#     print(payload)
#     print(type(payload))
# def create_a_pipeline(pipeline,namespace,payload)
# #创建多个技能
# def create_pipelines(namespace,pipelines=[]):
#     #实例化类
#     for i in pipelines:
#         pipeline = i['name']
#         payload = i['item']
#         create_a_pipeline(pipeline,'aliwebdev',payload)
#         time.sleep(1.5)
#