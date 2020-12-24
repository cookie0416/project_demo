import time
from util.mylog import MyLog
from configparser import ConfigParser
from ai_tools.executor import MyExecutor


def get_all_image_definition(namespace="test1"):
    """
    找到某个namespace下的所有组件的详细信息
    :param namespace:namespace
    :return:
    """
    my_executor = MyExecutor("ali")
    from_names = my_executor.get_all_image(namespace)['result']  # 找到ns下所有的组件名称["name2","name2"]
    from_imgs = my_executor.get_images_definition(from_names, namespace)  # 找到所有组件的详细信息
    return from_imgs


def delete_pipelines(pipelines=[], namespace="test1"):
    """
    删除多个技能（by pipeline name list）
    :param pipelines: 技能名称列表，eg:['pipeline-c457e083-aa9d-439e-b324-a374290fcf77','pipeline-4a4c9c03-b559-42ae-b78b-f41090eaa918']
    :param namespace:namespace
    :return:是否执行成功 True/False
    """
    my_executor = MyExecutor("ali")
    for pipeline in pipelines:
        my_executor.delete_pipeline(pipeline, namespace)  # 删除技能
        time.sleep(1.5)
    return True


def create_pipelines(pipelines=[], namespace="test1"):
    """
    创建多个技能
    :param pipelines: 技能名称列表，eg:['pipeline-c457e083-aa9d-439e-b324-a374290fcf77','pipeline-4a4c9c03-b559-42ae-b78b-f41090eaa918']
    :param namespace:namespace
    :return:是否执行成功 True/False
    """
    my_executor = MyExecutor("ali")
    for pipeline in pipelines:
        pipeline_name = pipeline['name']
        payload = pipeline['item']
        my_executor.create_a_pipeline(pipeline_name, payload, namespace)  # 创建技能
        time.sleep(1.5)
    return True


def get_pipelines_by_image(image, namespace):
    """
    找组件相关的所有技能,如果组件没有技能会被成功删除
    :param image: 组件名称 eg： 'parser-digital-format-check'
    :param namespace: namespace
    :return: pipelines_backup,技能的详细信息
    """
    my_executor = MyExecutor("ali")
    response = my_executor.delete_image(image, namespace)  # 先删除一次
    print(response)
    if not response:
        ids_str = response.json()["error"].split(': ', 1)[1]
        ids = ids_str.split(', ')  # 拿到所有的技能id——列表
        pipelines = my_executor.get_pipelines_definition(ids, 'aliwebdev')  # 找组件相关的所有技能
        pipelines_backup = pipelines['result']
    return pipelines_backup


def delete_image_and_related_pipelines(image, namespace):
    """
    删除某个组件以及相关的技能，返回删除的技能
    :param image: 组件名称 eg： 'parser-digital-format-check'
    :param namespace: namespace
    :return: pipelines_backup,技能的详细信息
    """
    my_executor = MyExecutor("ali")
    response = my_executor.delete_image(image, namespace)  # 先删除一次
    if not response:
        ids_str = response.json()["error"].split(': ', 1)[1]
        ids = ids_str.split(', ')  # 拿到所有的技能id——列表
        pipelines = my_executor.get_pipelines_definition(ids, 'aliwebdev')  # 找组件相关的所有技能
        pipelines_backup = pipelines['result']
        delete_pipelines(ids, 'aliwebdev')  # 删除技能
        my_executor.delete_image(image, namespace)  # 删除组件
    return pipelines_backup


def update_image(image, namespace):
    """
    更新一个组件，先删除后创建，会同步删除并重新创建组件相关的技能 （删技能-删组件-创建组件-创建技能）
    :param image: 组件名称 eg： 'parser-digital-format-check'
    :param namespace: namespace
    :return:是否执行成功 True/False
    """
    my_executor = MyExecutor("ali")
    backup = delete_image_and_related_pipelines(image, namespace)  # 删除组件以及相关的技能
    my_executor.create_image(image, namespace)  # 创建组件
    time.sleep(1.5)
    create_pipelines(backup, namespace)  # 创建技能
    return True


if __name__ == '__main__':
    # delete_pipelines(['pipeline-22088d57-6484-4f2e-89f4-c079cf1f5b97','pipeline-a9e35265-e8f8-469d-9c32-5f2fe8e74c42'],'aliwebdev')
    # my_executor = MyExecutor("ali")
    # my_executor.get_access_token()
    # my_executor.create_image('document-structure-extraction-v2','aliwebdev')
    # my_env = EnvRedeploy()
    # my_env.delete_pipelines(['pipeline-2d5bdc34-7b4a-49dd-97dd-78cb047e3a43','pipeline-32a48e99-43bb-4cb3-a784-608eedcb4444'],'aliwebdev')
    # delete_image_and_related_pipelines('document-structure-extraction-v2','aliwebdev')
    # update_image('document-structure-extraction-v2','aliwebdev')
    get_pipelines_by_image('document-structure-extraction-v2', 'aliwebdev')
    # pipelines = [{'name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf', 'item': {'models': [{'id': '37', 'names': ['document-structure-extraction-v2'], 'merge': {'parameters': {'query_value_ids': [], 'query_method': 'REGEXP', 'query_scopes': [], 'output_obj_type': 'PARAGRAPHS', 'query_value': '^(samsung|apple|huawei|xiaomi|vivo)', 'output_options': {'rows': [''], 'columns': ['']}, 'multi_match': True, 'output_content_type': 'PARAGRAPHS'}}}], 'created_date_time': '23-12-2020 11:06:49', 'created_ts': 1608721609328, 'metadata': {'display_name': 'updatetest1', 'version': '1.0', 'original_name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf'}}}, {'name': 'pipeline-59f2bc60-6c2d-4520-a04c-71ad78e218e3', 'item': {'models': [{'id': '37', 'names': ['document-structure-extraction-v2'], 'merge': {'parameters': {'query_value_ids': [], 'query_method': 'REGEXP', 'query_scopes': [], 'output_obj_type': 'PARAGRAPHS', 'query_value': '^(samsung|apple|huawei|xiaomi|vivo)', 'output_options': {'rows': [''], 'columns': ['']}, 'multi_match': True, 'output_content_type': 'PARAGRAPHS'}}}, {'id': '42', 'names': ['document-structure-extraction-v2'], 'merge': {}}], 'created_date_time': '23-12-2020 11:07:00', 'created_ts': 1608721620077, 'metadata': {'display_name': 'updatetest1', 'version': '2.0', 'original_name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf'}}}, {'name': 'pipeline-27ea5494-7209-4e6b-9cb6-97ec5f4c7b98', 'item': {'models': [{'id': '37', 'names': ['document-structure-extraction-v2'], 'merge': {'parameters': {'query_value_ids': [], 'query_method': 'REGEXP', 'query_scopes': [], 'output_obj_type': 'PARAGRAPHS', 'query_value': '^(samsung|apple|huawei|xiaomi|vivo)', 'output_options': {'rows': [''], 'columns': ['']}, 'multi_match': True, 'output_content_type': 'PARAGRAPHS'}}}, {'id': '42', 'names': ['document-structure-extraction-v2'], 'merge': {}}], 'created_date_time': '23-12-2020 12:29:40', 'created_ts': 1608726580390, 'metadata': {'display_name': '111111111', 'version': '3.0', 'original_name': 'pipeline-fb43c602-c55f-4205-ba81-0dd535b358bf'}}}]
    # get_all_image_definition('aliwebdev')
