import hashlib
import logging
import time
import traceback

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

data = None


def get_data():
    global data
    # China 疫情风险等级查询 url经过处理
    url = "******"

    timestamp = str(int(time.time()))
    nonceHeader = "123456789abcdefg"
    signatureHeaderStr = timestamp + "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA" + nonceHeader + timestamp
    signatureHeader = hashlib.sha256(signatureHeaderStr.encode(encoding="UTF-8")).hexdigest()

    payload = {
        "appId": "NcApplication",
        "paasHeader": "zdww",
        "timestampHeader": timestamp,
        "nonceHeader": nonceHeader,
        "signatureHeader": signatureHeader.upper(),
        "key": "3C502C97ABDA40D0A60FBEE50FAAD1DA"
    }
    signatureStr = timestamp + "fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA" + timestamp
    signature = hashlib.sha256(signatureStr.encode(encoding="UTF-8")).hexdigest()
    headers = {
        'x-wif-nonce': 'QkjjtiLM2dCratiA',
        'x-wif-paasid': 'smt-application',
        'x-wif-signature': signature.upper(),
        'x-wif-timestamp': timestamp,
    }

    response = requests.post(url, headers=headers, json=payload)

    logging.info(' ====> %s', response.text)
    response_json = response.json()
    if response_json['code'] == 0:
        # print(json.dumps(response_json, sort_keys=True, indent=2, ensure_ascii=False))
        print(f"最后更新时间: {response_json['data']['end_update_time']}")
        print(f"\t高风险个数: {response_json['data']['hcount']}")
        for high in response_json['data']['highlist']:
            print(f"\t\t地区: {high['area_name']}")
            print(f"\t\t城市: {high['city']}")
            print(f"\t\t社区: {', '.join(high['communitys'])}")
            print(f"\t\t县: {high['county']}")
            print(f"\t\t省: {high['province']}")
            print(f"\n")
        print(f"\t中风险个数: {response_json['data']['mcount']}")
        for middle in response_json['data']['middlelist']:
            print(f"\t\t地区: {middle['area_name']}")
            print(f"\t\t城市: {middle['city']}")
            print(f"\t\t社区: {', '.join(middle['communitys'])}")
            print(f"\t\t县: {middle['county']}")
            print(f"\t\t省: {middle['province']}")
            print(f"\n")


if __name__ == '__main__':
    err = 0
    while True:
        try:
            get_data()
            time.sleep(60 * 60)
        except Exception as e:
            # traceback.print_exc()
            err += 1
            logging.error('------- error -----> %s', e)
            "send_msg('监控风险地区有异常', str(traceback.format_exc()))" if err <= 3 else sys.exit(0)
            time.sleep(60)

#