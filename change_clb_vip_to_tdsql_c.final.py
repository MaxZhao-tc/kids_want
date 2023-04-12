from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cynosdb.v20190107 import cynosdb_client, models
import os
import time
import json
import datetime
# 从配置文件导入数据
from config import SecretId, SecretKey, CLB_ID, TDSQL_ID, DTS_ID, VIP


def check_clb(clbId):
    from tencentcloud.clb.v20180317 import clb_client, models
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "clb.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = clb_client.ClbClient(cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeLoadBalancersRequest()
        params = {
            "LoadBalancerIds": [clbId]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeLoadBalancersResponse的实例，与请求对象对应
        resp = client.DescribeLoadBalancers(req)
        # 输出json格式的字符串回包
        # print(resp.to_json_string())
        instance_data_obj = json.loads(resp.to_json_string())
        InstanceData = instance_data_obj['TotalCount']
        # InstanceTotalCount=
        return InstanceData

    except TencentCloudSDKException as err:
        print(err)


def get_clb_vip(clbId):
    from tencentcloud.clb.v20180317 import clb_client, models
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "clb.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = clb_client.ClbClient(cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeLoadBalancersRequest()
        params = {
            "LoadBalancerIds": [clbId]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeLoadBalancersResponse的实例，与请求对象对应
        resp = client.DescribeLoadBalancers(req)
        # 输出json格式的字符串回包
        # print(resp.to_json_string())
        instance_data_obj = json.loads(resp.to_json_string())
        InstanceData = instance_data_obj['LoadBalancerSet']
        InstanceVips = InstanceData[0]['LoadBalancerVips'][0]
        return InstanceVips

    except TencentCloudSDKException as err:
        print(err)


def delete_clb(clbId):
    from tencentcloud.clb.v20180317 import clb_client, models
    """delete clb"""
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "clb.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = clb_client.ClbClient(cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DeleteLoadBalancerRequest()
        params = {
            "LoadBalancerIds": [clbId]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DeleteLoadBalancerResponse的实例，与请求对象对应
        resp = client.DeleteLoadBalancer(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def GetTdsql_C_GrpId(ClusterId):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cynosdb.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = cynosdb_client.CynosdbClient(
            cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeClusterInstanceGrpsRequest()
        params = {
            "ClusterId": ClusterId
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeClusterInstanceGrpsResponse的实例，与请求对象对应
        resp = client.DescribeClusterInstanceGrps(req)
        # 输出json格式的字符串回包
        # print(resp.to_json_string())

        instance_data_obj = json.loads(resp.to_json_string())
        InstanceGrpInfoListData = instance_data_obj['InstanceGrpInfoList']
        InstanceGrpId = InstanceGrpInfoListData[0]['InstanceGrpId']
        # instance_info = jsonpath.jsonpath(instance_data_obj, '$..InstanceGrpId')
        return InstanceGrpId

    except TencentCloudSDKException as err:
        print(err)


def ModifyVipVportTdsql_C(ClusterId, InstanceGrpId, Vip):
    """ModifyVipVport for Tdsql_C"""
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cynosdb.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = cynosdb_client.CynosdbClient(
            cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ModifyVipVportRequest()
        params = {
            "ClusterId": ClusterId,
            "InstanceGrpId": InstanceGrpId,
            "Vip": Vip,
            "Vport": 3306,
            "OldIpReserveHours": 0
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个ModifyVipVportResponse的实例，与请求对象对应
        resp = client.ModifyVipVport(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)

# 检查 dts 延迟时间
def check_dts(dts_id):
    value = -1
    from tencentcloud.monitor.v20180724 import monitor_client, models
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "monitor.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = monitor_client.MonitorClient(cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.GetMonitorDataRequest()
        # start_time 和 end_time 取 当前时间的前 90s
        now = datetime.datetime.now()
        start_time = now - datetime.timedelta(seconds=90)
        start_time = start_time.astimezone().replace(microsecond=0).isoformat()
        end_time = now.astimezone().replace(microsecond=0).isoformat()
        print ("start_time: %s, end_time %s" % (start_time, end_time))
        params = {
            "Namespace": "QCE/DTS",
            "MetricName": "MigrateLag",
            "Period": 60,
            "StartTime": start_time,
            "EndTime": end_time,
            "Instances": [
                {
                    "Dimensions": [
                        {
                            "Name": "migratejob_id",
                            "Value": dts_id,
                        }
                    ]
                }
            ]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个GetMonitorDataResponse的实例，与请求对象对应
        resp = client.GetMonitorData(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())
        resp_data_obj = json.loads(resp.to_json_string())
        print(resp_data_obj)
        if "DataPoints" in resp_data_obj and resp_data_obj["DataPoints"] is not None and len(resp_data_obj["DataPoints"]) > 0:
            data_point = resp_data_obj["DataPoints"][0]
            if "Values" in data_point and data_point["Values"] is not None and len(data_point["Values"]) > 0:
                value = data_point["Values"][0]

    except TencentCloudSDKException as err:
        print(err)

    return value

# 判断 IP 是否可以 ping 通, 适用于linux系统, windows系统参数需调整
def is_pingable(ip_address):
    result = os.system('ping -c 1 -w 1 %s >/dev/null 2>&1' % ip_address)
    return result == 0

# 检查 TDSQL VIP 是否绑定成功， 返回 True 即为绑定成功，返回 False 即为 绑定失败
def check_TDSQL_VIP(ClusterId, VIP):
    check_TDSQL_VIP_status = False
    from tencentcloud.cynosdb.v20190107 import cynosdb_client, models
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cynosdb.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = cynosdb_client.CynosdbClient(cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeClusterDetailRequest()
        params = {
            "ClusterId": ClusterId
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeClusterDetailResponse的实例，与请求对象对应
        resp = client.DescribeClusterDetail(req)
        # 输出json格式的字符串回包
        # print(resp.to_json_string())
        resp_data_obj = json.loads(resp.to_json_string())
        if "Detail" in resp_data_obj and resp_data_obj["Detail"] is not None:
            detail = resp_data_obj["Detail"]
            if "Vip" in detail and detail["Vip"] is not None:
                check_TDSQL_VIP_status = detail["Vip"] == VIP


    except TencentCloudSDKException as err:
        print(err)

    return check_TDSQL_VIP_status

def main():
    InstanceGrpId = GetTdsql_C_GrpId(TDSQL_ID)
    clb_status = check_clb(CLB_ID)
    # 记录是否执行了 删除 CLB 操作
    delete_opt_flag = False
    if clb_status == 1:
        # 循环检查 dts 延迟时间 10 次，每次间隔 1s
        check_dts_count = 10
        check_dts_interval = 1
        while check_dts_count > 0:
            check_dts_result = check_dts(DTS_ID)
            if check_dts_result == 0:
                print("dts delay is 0, start delete CLB, ID: %s" % CLB_ID)
                delete_clb(CLB_ID)
                delete_opt_flag = True
                break
            check_dts_count = check_dts_count - 1
            time.sleep(check_dts_interval)  # 间隔时间

    # 执行了删除操作，则循环 检查 CLB 是否已被删除以及IP是否被释放
    bind_TDSQL_opt_flag = False
    if delete_opt_flag:
        # 循环检查 clb 是否已删除、IP是否已释放 10 次，每次间隔 1s
        remain_check_clb_count = 10
        check_clb_interval = 1
        while remain_check_clb_count > 0:
            deleted_clb_status = check_clb(CLB_ID)
            deleted_clb_ip = is_pingable(VIP)
            print("remain_check_clb_count: %d, deleted_clb_status: %d, deleted_clb_ip: %s" % (remain_check_clb_count, deleted_clb_status, str(deleted_clb_ip)))
            # 当 clb 被删除 并且 IP 无法 ping 通时，说明 IP 已被释放，可以绑 TDSQL
            if deleted_clb_status == 0 and deleted_clb_ip is False:
                print("CLB ID: %s has been deleted, IP: %s has been released，start first bind TDSQL" % (CLB_ID, VIP))
                ModifyVipVportTdsql_C(TDSQL_ID, InstanceGrpId, VIP)
                bind_TDSQL_opt_flag = True
                print("first bind TDSQL end")
                break
            remain_check_clb_count = remain_check_clb_count - 1
            time.sleep(check_clb_interval)  # 间隔时间
    else: 
        print("delete CLB failed, exit")

    # 执行了第一次绑定 TDSQL 操作后，轮询是否绑定成功，如果不成功则继续尝试绑定 TDSQL
    if bind_TDSQL_opt_flag:
        # 循环检查 TDSQL 是否绑定成功 6 次，每次间隔 10s
        remain_check_TDSQL_VIP_count = 6
        check_TDSQL_VIP_interval = 10
        # 第一次操作后也要等待 5s，sleep 的操作放在最前面
        while remain_check_TDSQL_VIP_count > 0:
            time.sleep(check_TDSQL_VIP_interval)  # 间隔时间
            check_TDSQL_VIP_status = check_TDSQL_VIP(TDSQL_ID, VIP)
            print("remain_check_TDSQL_VIP_count: %d, check_TDSQL_VIP_status: %s" % (remain_check_TDSQL_VIP_count, check_TDSQL_VIP_status))
            if check_TDSQL_VIP_status:
                print("bind TDSQL success")
                break
            else:
                print("try bind TDSQL")
                ModifyVipVportTdsql_C(TDSQL_ID, InstanceGrpId, VIP)
            
            remain_check_TDSQL_VIP_count = remain_check_TDSQL_VIP_count - 1
            

    else:
        print("first bind TDSQL failed, exit")

if __name__ == '__main__':
    main()
