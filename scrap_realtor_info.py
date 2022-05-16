import requests
import re
import pandas as pd

RealtorName = []
RealtorPosition = []
OfficeName = []
OfficeAddress = []
PhoneNumber = []

for i in range(1,31):
    url = 'https://www.realtor.ca/Services/ControlFetcher.asmx/GetRealtorResults'

    data = '{addressLine1: "", city: "", companyName: "", currentPage: "i", designations: "", firstName: "", isCCCMember: "", languages: "", lastName: "", maxRecords: null,organizationId: "",postalCode: "",provinceIds: "",recordsPerPage: 20,showOfficeDetails: null,sortBy: "11",sortOrder: "A",specialties: ""}'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.360',
              'cookie': '__AntiXsrfToken=e6e4feb3de974528b6a98bc6b64efe80; Language=1; app_mode=1; Currency=CAD; Province=Ontario; Country=Canada; cmsdraft=False; GUID=0af16e09-1bcc-4933-9346-e29401ecb3b8; visid_incap_2269415=wTHrGUx9Rg2K8z/A404xZBcNEWIAAAAAQUIPAAAAAABmdfz4I6WmEFiU60LwufbC; nlbi_2269415=Q9EdYp5eZk3FBlfBkG5lugAAAADsMndfZM0LmUWWo8jeUZrN; incap_ses_1444_2269415=P9Ddcdtq8X0F8CADlh4KFBcNEWIAAAAA15kIyAucR5TNLXh4uSzKNg==; ai_user=vX2eq|2022-02-19T15:30:38.562Z; _gid=GA1.2.853409348.1645284641; gig_canary=false; _fbp=fb.1.1645284646380.1360876160; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; incap_ses_886_2269415=p8dBBi2ys3ukZcH84LRLDBIQEWIAAAAA3bwvKmG1bu+bdXx1mNAVkA==; visid_incap_2271082=5LOtp+9CTpC1hXVczguZjhIQEWIAAAAAQUIPAAAAAAA2o2tXRVjNUxml5QHiglqD; nlbi_2271082=h6FieEEUqzC2dzAPcbDG1QAAAAAHl7vOsZKabWhEYjT0n1Qx; incap_ses_886_2271082=b0MCISzVPHAfZ8H84LRLDBMQEWIAAAAAnuzWa5talVF5ADgva/n4ww==; reese84=3:pelSEQLKzkzvE+/tBCuiAw==:AXel1NUGtp4NWcmwHqWpwIN9D/6Ta3ypeTbuB6tDY38LONvyQfTmedsKtGoVAEm7Gd1POCxiogfDCoUQnWKr48IWn7SQ6if7RJtN2kfMdzWWEhx8LWVA8id/9JaBmV52/lY34COilhYqlE/ljh/VrSQRHu0duRBE8+LF+a9Wh+BN6VYYAdlz/A6q2vcuwR6Vj6ujDixVeNgB8vG1VET1kzDua8x8rOGlWMj2jx0pY9BwK1vgqi+EoA8VSf9VFOjdbrkcO3CgwEafRd5s7tIeJTa6tVlkVpVgt0LK8azlhqqwBa3CU0BMUbWsSUgBI9FfQiZuvE4VrfKCel9bhWdsEHKihCLi76qEam/NKWWmlnjMwzaLwxx/dPnTUn8DNcuLWzJnpDZhXQffYz+ygKPtMWo7v3EHpv0moetTqbikDptv6teuzNMD9hd4nQitbwrC:GJd0N+DiDYzho0nLQH+YfbfI7SEOZYRcWbsEH56rF0M=; _ga=GA1.1.990480238.1645284641; _ga_Y07J3B53QP=GS1.1.1645284639.1.1.1645285760.59; ai_session=Fn9qG|1645284642240|1645285761180.3; gig_canary_ver=12852-3-27421425; _4c_=%7B%22_4c_s_%22%3A%22jVNdj9owEPwrJz9jiB3HH7xVVKpOuqpV1aqPJ2M7xCLEkWNI7078964hwOmulY6HYE92Jruzuy9obFyHloSzikpeVJUq5Qxt3dOAli8oepv%2FDmiJhBWyKgTHbl1WmNUVxZK7ChNjnDZG2poTNEN%2FTlpCClEqpYSYoZRatKSVosXpd5wh00%2BiL8gE60CcqDlhc1LgegCN9AwQLosCzn0Mdm%2FSY3rqc%2BDo1neD3cIL6w7euMfR29ScFGhxQxvnN03KcCFPcB%2FzBU6j72wYrzTJxQ28slSZ0XUM4%2BAycdXEsHN3SgIawBj0%2B0TIuUZXuxhPUU1K%2FbBcLMZxnG9C2LRubsJuAUGDTzn56HSbQpwbPWFg8w3GJ%2FhBd5u93rgp3Yew2Th7dw8tQrVuBwfY9xgOvjM55FuXdPQBwFXYdylmuZXutM1SP9zgreuS122Iq7DbueiNbl8p9bmxHA5tgBdZEGZhBo%2BM99HC%2Bcunx1%2F3n7MnqmCyoKWcn2eFcZYT3Mf2Tem3KhdQR5cWtFBUULEwvnv2Gre%2B01ArmJaSxpQIha3u6hBTg%2FXBYeCGLgUczrXhHTNky7JjziQfuptjgP2MHgyKX11qAowq3LX1OQrqhLbnYOtqvW9TvubemlYPgzfWDdsUenS8jGxVCko4hbGdRlZydhnY%2FjANLH8VDYlXVMn30ZM0vvTVdf%2Flw4y%2F5x%2F8ZeeYlETwwuD1mjDM1q7E0miNVeG4hmSZ1va6c9ATUXEiKJ0kibxlVF8lqYJtVRwLXVNMiDOgZjkuKKPakLykJXqTpfqXJ9nbs%2BTN4I8sv%2B%2FTRDznXJVKMEY%2FSL5%2B80NfOx7%2FAg%3D%3D%22%7D; nlbi_2269415_2147483392=qHStZZ0SnT8oxR09kG5lugAAAADtj7nYGxwaXOQvA+/ywrYx',
              'referer': 'https://www.realtor.ca/realtor-search-results',
              'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,und;q=0.6,fr;q=0.5',
               'content-type': 'application/json; charset=utf-8'}
    res = requests.post(url,data=data, headers=headers)
    ret = res.text.replace('\\n',"").replace('\\r',"").replace("\\u003c","").replace('\\u003e',"").replace('\\u0026',"")
    pattern = re.compile('innertext=RealtorName\\\\"(.*?)\/span.*?innertext=RealtorPosition\\\\"\s+(.*?)\s+\/div.*?innertext=OfficeName\\\\"\s+(.*?)\s+\/div.*?innertext=OfficeAddress\\\\"\s+(.*?)\s+\/div.*?TelephoneNumber\\\\"(\d{3}-\d{3}-\d{4})')
    datas = pattern.findall(ret)
    for data in datas:
        RealtorName.append(data[0])
        RealtorPosition.append(data[1])
        OfficeName.append(data[2])
        OfficeAddress.append(data[3])
        PhoneNumber.append(data[4])

df = pd.DataFrame({'Realtor Name': RealtorName,'Realtor Position': RealtorPosition, 'OfficeName':OfficeName, 'Office Address': OfficeAddress,'Phone Number':PhoneNumber})
df.to_csv('realtors.csv')

