import csv 
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import uuid

import json

def workday_scrape():
    # Load or initialize job_ids_dict from file
    try:
            with open('job_ids_dict.pkl', 'rb') as f:
                    job_ids_dict = pickle.load(f)
    except FileNotFoundError:
            job_ids_dict = {}

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    #company_urls = []
    company_urls_dict = {
    'https://expedia.wd5.myworkdayjobs.com/en-US/search/?q=software&locations=0210e11067580172e7b490ef4646e32e&locations=c553432013ba103bbc5ad359b6015015&locations=d4592151fa8e100bf6713848a881ae87': "Expedia",
    'https://rb.wd5.myworkdayjobs.com/FRS?q=software': "Federal Reserve",
    'https://sec.wd3.myworkdayjobs.com/Samsung_Careers?q=software&locations=189767dd6c9201f478822b84a5296379&locations=189767dd6c920127c1bb2284a5295979&locations=89abf27ec3f61038a12cbd91f1e80000&locations=189767dd6c9201733cceee83a5291d79&locations=189767dd6c92012532fbf283a5292279&locations=189767dd6c9201deb3d8b181a529e375&locations=189767dd6c9201b2f53c9686a529647c&locations=189767dd6c9201c7fed64881a5295975&locations=31fc7bab264601f2a48f9e5ec5243c60&locations=502ab515a87601e1dd395608ad1e7f3b&locations=189767dd6c9201de7df2a581a529d475&locations=f0594f1b6e8110018479afa655870000&locations=189767dd6c9201d24193c587a529ed7d&locations=189767dd6c9201d2eed84985a529c87a&locations=189767dd6c920124d517b483a529d778&locations=b3de64aa962d1014d12136a4258f0000&locations=189767dd6c920132898dee88a529647f&locations=280e1f8498650160a2135cb2400dbd0c': "Samsung",
    'https://washpost.wd5.myworkdayjobs.com/washingtonpostcareers?q=software&locations=4304a0380a52012c74f3e3e27654ff92': "The Washington Post",
    'https://crowdstrike.wd5.myworkdayjobs.com/crowdstrikecareers?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Crowdstrike",
    'https://zoom.wd5.myworkdayjobs.com/Zoom/?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Zoom",
    'https://generalmotors.wd5.myworkdayjobs.com/Careers_GM?locations=db7780503a74016716567709b71f521d&locations=ef70808648fe01f31123ba650305fb3d&locations=e30192a1b9ad0124a3ccb0adb61fdd4c&locations=b0be2c0a966710016c9654dbd0010000&locations=e30192a1b9ad01f018f447afb61fec4c&locations=5e70e1905c63014231f3200ab71f8c14&locations=6111e68864d501e35a86a30fb71f1139&locations=5e70e1905c63014a9deb370ab71f9114&locations=88b46ead68660104cd31488ab559f264&locations=812c98c9baa4018b0edd880ab71ffc2b&locations=983c57f4d0d8014366f17425581d939e&locations=88b46ead6866013c0488b18ab559f764&locations=812c98c9baa4014ab256b80ab71f012c&locations=d4e1946d0ed40182b528810bb71fe013&locations=5e70e1905c63014b2885e80ab71fa014&locations=812c98c9baa4014b13222e0bb71f072c&locations=608c920536e910016db8acc82a590000&locations=107799e78de4010793c4bb6fb8599963&locations=d4e1946d0ed401cc9f679a08b71fcc13&locations=899fdb5109a8014dc08020afb61fd238&locations=e30192a1b9ad01e80c23deacb61fc94c&locations=e30192a1b9ad01b8ed4dffacb61fce4c&locations=107799e78de401742c495a6fb8598a63&locations=983c57f4d0d8010ea058b125581dca9e&locations=6111e68864d5017999ca520cb71ff338&locations=812c98c9baa401e717e2c606b71fd92b&locations=e30192a1b9ad0131eb632cacb61fba4c&locations=2f3d18c6c1cd018cd8d14867b859af9f&locations=5e70e1905c63013cbc667506b71f6914&locations=5e70e1905c63016dca365006b71f5f14&locations=899fdb5109a801b4b7ab82adb61faf38&locations=e30192a1b9ad01b3b30272abb61faf4c&locations=983c57f4d0d801919ecff82b581d39a4&locations=d4e1946d0ed401c398089d06b71fbd13': "General Motors",
    'https://carmax.wd1.myworkdayjobs.com/External/?q=software': "CarMax",
    'https://boeing.wd1.myworkdayjobs.com/MFG?q=software': "Boeing",
    'https://workiva.wd1.myworkdayjobs.com/careers?q=software&locations=75715069c97201653aadd113f32bf85c&locations=75715069c972010772aec813f32be45c&locations=75715069c97201d09d6f4c14f32ba65e&locations=75715069c972018a0bfdd213f32bfd5c&locations=75715069c97201c98e6c4514f32b8d5e&locations=75715069c972012c54391014f32bcf5d&locations=75715069c972014492720814f32bc05d&locations=75715069c9720100a8301e14f32bf75d&locations=75715069c97201ab5f0e2a14f32b245e&locations=75715069c97201a7609d2c14f32b2e5e&locations=75715069c97201ffbc593014f32b3d5e&locations=75715069c972016b2e693414f32b4c5e&locations=75715069c972011875853a14f32b655e&locations=57a493ba6929014c2e93af43c2007b6c': "Workiva",
    'https://disney.wd5.myworkdayjobs.com/en-US/disneycareer/?locations=4f84d9e8a09701011a71d2e0e0e50000&locations=4f84d9e8a09701011a72ab74b16d0000&locations=4f84d9e8a09701011a58c36993630000&locations=4f84d9e8a09701011a666ce5d46a0000&locations=4f84d9e8a09701011a66448e51f30000&locations=4f84d9e8a09701011a5948763c4b0000&locations=4f84d9e8a09701011a5a3cea04650000&locations=4f84d9e8a09701011a5e0d8577e40000&locations=4f84d9e8a09701011a6ded3d6b520000&locations=4f84d9e8a09701011a6ff52600b00000&locations=4f84d9e8a09701011a59d726dbab0000&locations=4f84d9e8a09701011a762a24b0900000&locations=4f84d9e8a09701011a69fd38359c0000&locations=4f84d9e8a09701011a595216d7b20000&locations=4f84d9e8a09701011a6f6d34a6070000&locations=4f84d9e8a09701011a5b2c8df7e60000&locations=4f84d9e8a09701011a6afaad40e30000&locations=4f84d9e8a09701011a58839baa360000&locations=4f84d9e8a09701011a6f4c1aa3860000&locations=4f84d9e8a09701011a75aec3e82c0000&locations=4f84d9e8a09701011a5a6a0fddb20000&locations=4f84d9e8a09701011a59a3f706480000&locations=4f84d9e8a09701011a5e034bd6650000&locations=4f84d9e8a09701011a73b611c43c0000&locations=4f84d9e8a09701011a577e62d20b0000&locations=4f84d9e8a09701011a740910665e0000&locations=4f84d9e8a09701011a568bcec9810000&locations=4f84d9e8a09701011a69f86739820000&locations=4f84d9e8a09701011a73185a110e0000&locations=4f84d9e8a09701011a5fa89789280000': "Disney",
    'https://regeneron.wd1.myworkdayjobs.com/Careers?q=software': "Regeneron",
    'https://wd3.myworkdaysite.com/en-US/recruiting/takeaway/grubhubcareers?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Grubhub",
    'https://cigna.wd5.myworkdayjobs.com/cignacareers?q=software&Location_Country=bc33aa3152ec42d4995f4791a106ed09': "Cigna",
    'https://comcast.wd5.myworkdayjobs.com/en-US/Comcast_Careers/?q=software': "Comcast",
    'https://target.wd5.myworkdayjobs.com/targetcareers?q=software&Location_Country=bc33aa3152ec42d4995f4791a106ed09': "Target",
    'https://sonyglobal.wd1.myworkdayjobs.com/SonyGlobalCareers?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Sony",
    'https://dell.wd1.myworkdayjobs.com/External/?q=software&Location_Country=bc33aa3152ec42d4995f4791a106ed09': "Dell",
    'https://proofpoint.wd5.myworkdayjobs.com/ProofpointCareers?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Proofpoint",
    'https://lowes.wd5.myworkdayjobs.com/LWS_External_CS?q=software': "Lowes",
    'https://db.wd3.myworkdayjobs.com/DBWebsite/?q=software&Country=bc33aa3152ec42d4995f4791a106ed09': "Deutsche Bank",
    'https://haier.wd3.myworkdayjobs.com/GE_Appliances?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'GE Appliances',
    'https://globalhr.wd5.myworkdayjobs.com/REC_RTX_Ext_Gateway/?q=usa%20software': "Raytheon",
    'https://stryker.wd1.myworkdayjobs.com/StrykerCareers?q=software&Location_Country=bc33aa3152ec42d4995f4791a106ed09': "Stryker",
    'https://verizon.wd5.myworkdayjobs.com/verizon-careers?q=software': "Verizon",
    'https://kohls.wd1.myworkdayjobs.com/kohlscareers/?q=software': "Kohl's",
    'https://geico.wd1.myworkdayjobs.com/External?q=software': "Geico",
    'https://accenture.wd3.myworkdayjobs.com/AccentureCareers/?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Accenture",
    'https://northwesternmutual.wd5.myworkdayjobs.com/CORPORATE-CAREERS/?q=software': "Northwestern Mutual",
    'https://boseallaboutme.wd1.myworkdayjobs.com/Bose_Careers/jobs?q=software&locations=eff671d2c9a90121f644028f894965bd&locations=525231f0186e0117821dc4641b2459de&locations=61fc0dd0d435018a4474dc689a11aa2a&locations=31b7f9e93b0f10995df07be31d403844&locations=31b7f9e93b0f10995df08a4feca03862&locations=31b7f9e93b0f10995df085940a703858&locations=c286d09839da010d3342d8a79a599c38': "Bose",
    'https://warnerbros.wd5.myworkdayjobs.com/global/?q=software&locations=13aa073be65f100162b4648160b90000&locations=d3a1c2776673102ed9eb8adafc1a9bf3&locations=d3a1c2776673102ed9e6e7cf1aaa968d&locations=f91d2ab82c75017d70bc358115208c81&locations=f91d2ab82c75019ebc04268115208081&locations=f91d2ab82c75013c49aff0821520ee82&locations=f91d2ab82c7501f21d9e3c8315202a83&locations=d3a1c2776673102ed9e77d39ddfa9782&locations=0cf7b3f170ed01f72b864522362ec91d&locations=d3a1c2776673102ed9eb486275a29b8f&locations=730b16ca350f01064be2e049269b0000&locations=e7f67d9b72630123638b3ae4356a0000&locations=d3a1c2776673102ed9ee946a6f6a9ec0&locations=26783a8ba1241001f61fa85f960b0000&locations=433ba06365f101ea3dba1c6b5a1db805&locations=a426938d4cbe105994f41eb1513a75f9&locations=d3a1c2776673102ed9e8fea5c65a98a5&locations=d3a1c2776673102ed9e90d85c9ea98c3&locations=d3a1c2776673102ed9e910003fca98c8&locations=d3a1c2776673102ed9e929b7843298fa&locations=d3a1c2776673102ed9e94eabb8b29940&locations=d3a1c2776673102ed9e951344bda9945&locations=d3a1c2776673102ed9e966ac6baa9972&locations=d3a1c2776673102ed9e9700419329986&locations=d3a1c2776673102ed9eacaeb90229aa4&locations=a7052702ae74016e949a9061140146ca&locations=d3a1c2776673102ed9eb43270eea9b85&locations=823b58a1540d1001f63c0d42fa750000&locations=a39cd315cbaf100d16b618f27c90ddb9&locations=2d864b3b2db91000c8426462abf40000': 'Warner Bros',   
    'https://vanguard.wd5.myworkdayjobs.com/vanguard_external/?q=software': 'Vanguard',
    'https://pru.wd5.myworkdayjobs.com/en-US/Careers/?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'Prudential',
    'https://cat.wd5.myworkdayjobs.com/en-US/CaterpillarCareers?q=software': "Caterpillar",
    'https://discover.wd5.myworkdayjobs.com/Discover/?q=software&locations=febd73641484109bf1faaa7e997a66c3&locations=96bf16fa269701eb4279010ddf93b1e3&locations=dd81500376e3100d308a99d97cab4fb9&locations=dd81500376e3100d308a95535c334faf&locations=dd81500376e3100d308a6dcac9034f5a': "Discover",
    'https://citi.wd5.myworkdayjobs.com/en-US/Citi_Early_Careers_Events_Site?locations=6669335a15de01102f237d2361002d8e': 'Citi',
    'https://mastercard.wd1.myworkdayjobs.com/en-US/CorporateCareers?q=software&locations=efacbd97fd67011dbc0f236fbb007b75&locations=8eab563831bf10acbcb35b24fcd616d7&locations=8eab563831bf10acbbdb817a833d0fa6&locations=8eab563831bf10acbba0ec70e0f00d06&locations=c9c1221064f54d28ae6ab893b99923cf&locations=4345730331e1457585f99e8c7feb2c84&locations=933510b9c63001db6f2742d309148e2e&locations=85482cdd21931001b922354af3a90000&locations=a52da795b81f100109d635958d730000&locations=3b2ad45f5eca10bd534be5fa946139c3&locations=8eab563831bf10acb54f0f21651ed219': 'Mastercard',
    'https://intel.wd1.myworkdayjobs.com/en-US/External?q=software&locations=1e4a4eb3adf1019877cb6176bf81fdce&locations=1e4a4eb3adf1011246675c76bf81f8ce&locations=9225dd5a24931001586f2d984f1e0000&locations=1e4a4eb3adf10146fd5c5276bf81eece&locations=1e4a4eb3adf101d4e5a61779bf8159d1&locations=1e4a4eb3adf10155d1cc0778bf8180d0&locations=1e4a4eb3adf10118b1dfe877bf8162d0&locations=1e4a4eb3adf10129d05fe377bf815dd0&locations=1e4a4eb3adf1013ddb7bd877bf8153d0&locations=1e4a4eb3adf1018c4bf78f77bf8112d0&locations=1e4a4eb3adf101b8aec18a77bf810dd0&locations=1e4a4eb3adf1016541777876bf8111cf&locations=1e4a4eb3adf101770f350977bf8193cf&locations=1e4a4eb3adf10174f0548376bf811bcf&locations=1e4a4eb3adf101cc4e292078bf8199d0': 'Intel',
    'https://trimble.wd1.myworkdayjobs.com/en-US/TrimbleCareers/?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'Trimble',
    'https://workday.wd5.myworkdayjobs.com/Workday/?q=software&locations=9da5d518486801f61a50c4aedf1ab23f&locations=3ab10dbed327011d15b12a84e99f0000&locations=62a48cfecb41101e2011999af07c4fdb&locations=4d3a30f878c5011d15d8cafbd5810000&locations=79dc078ddcd3011d15d948875a540000&locations=2213391f747b10c033902db2a95c0d54&locations=b9e1bd0308fa45c99ffb2a213df4ea89&locations=4a495540e231011d159e2a1748d20000&locations=8de299d6807c4b728fff741af567fdd2&locations=63f4787825e34e7489c2daf345a6eeca&locations=7ae44bd8a8dd011d159d95802f800000&locations=4d3a30f878c5011d15d84d49396b0000&locations=37d28f4bbdbd4d2eb17797f5a1fdde64&locations=ee00a5e27c4d011d159d790ec0780000&locations=8368f8b8807f4f4eb52a11debc5dbc78&locations=3ab10dbed327011d15b0690b92090000&locations=4e31200cd95b011d159b6b64027d0000&locations=84e4bb4fde894383a0dbe933bed4bfac&locations=ee00a5e27c4d011d159d20a6bc6b0000&locations=03ad8e81362b011d159c7e2f176b0000&locations=1f451b161f8b405487e7ebe5c0a13d6b&locations=4e31200cd95b011d159aae50da030000&locations=4d3a30f878c5011d15d7497ff49c0000&locations=4d3a30f878c5011d15d73ba986380000&locations=3156cbdb27884558ab0cd50910ec861d&locations=4e31200cd95b011d159a481bb4f10000&locations=e0e149b40d964e5fb845f6087d90a63c&locations=ee00a5e27c4d011d159c1d8b065d0000&locations=09149267bc324fccba44db134da36767&locations=79dc078ddcd3011d15d744139a6a0000&locations=79dc078ddcd3011d15d736bf3eaa0000&locations=4e31200cd95b011d1599e64428670000&locations=3ab10dbed327011d15aec723e0a00000&locations=3a7c96b9fb264d0492ef8899556f58a7&locations=9821e80f698e10fe45f138d1947cc62f&locations=289a125164674dd28c79bc9bb7e46fd8&locations=3ab10dbed327011d15aeab6561190000&locations=5e834d290de7475ba43b61959f6a9d1c&locations=ee7b6c3463e042e0987338c98618312a&locations=7ae44bd8a8dd011d159b9178d7bd0000&locations=ee00a5e27c4d011d159b64d2ff450000&locations=4dddc4fa2321433bb47dee7fb2ead6ec&locations=71646621170f01ae159ce0c1dd1a273b': 'Workday',
    'https://ouryahoo.wd5.myworkdayjobs.com/careers?q=software&locations=429c19fc6ff810015940b81d49a00000': 'Yahoo',
    'https://vmware.wd1.myworkdayjobs.com/VMware/1/refreshFacet/318c8bb6f553100021d223d9780d30be': 'VMware',
    'https://wabtec.wd1.myworkdayjobs.com/wabtec_careers': 'Wabtec',
    'https://wd1.myworkdaysite.com/en-US/recruiting/snapchat/snap?q=software&locations=95d6b3b2e7d91001614ca11093850000&locations=256f279d5e741082c567c24fca236272&locations=efe1a865073101b9db6c8da7020a6037&locations=7a68e5b6d6b51001a9de39167c5f0000&locations=b9cf6982655e1001a9ff7ae350d10000&locations=8bf70c1877bb01f58a864a033aab9149&locations=efe1a865073101e5380680f9020a7437&locations=efe1a86507310187e01ef207030a7937&locations=2b0a835c9646011d58da08236e4f6726&locations=fad1b9bbc305019817878678061de155&locations=1763d6f1e9be01bf7a8548e05b4da26e&locations=efe1a865073101717b72c224020a0137&locations=f84c7a1ec2ba1000d7878e08800c0000&locations=b6d8d8a3809d10016c27d22429420000&locations=c52c83bb81a21000cf303bd607c00000&locations=a47fe10a5e6210b95624c5690b522fe0&locations=efe1a865073101ddec60ef19020afc36&locations=efe1a8650731016c130aaddd010aed36': 'Snapchat',
    'https://att.wd1.myworkdayjobs.com/ATTGeneral?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'AT&T',
    'https://twitter.wd5.myworkdayjobs.com/en-US/X?q=software&source=XCareers&locations=62c0f5a23a3d10012a6f03fc66fd0000&locations=62c0f5a23a3d10012a6efcb9574b0000&locations=62c0f5a23a3d10012a6ef445e83e0000&locations=62c0f5a23a3d10012a6eebd5e2bf0000&locations=474d5e24607610012a6d2726d1a10000&locations=474d5e24607610012a6d1ce717500000&locations=62c0f5a23a3d10012a6f7a9588e40000&locations=474d5e24607610012a6d13432d5f0000&locations=474d5e24607610012a6d0ad128ec0000&locations=62c0f5a23a3d10012a6cddc6a9510000&locations=62c0f5a23a3d10012a6cc9ebcd760000': 'Twitter',
    'https://pnc.wd5.myworkdayjobs.com/en-US/External?q=software': 'PNC',
    'https://ghr.wd1.myworkdayjobs.com/en-US/Lateral-US?q=software': 'Bank of America',
    'https://blackstone.wd1.myworkdayjobs.com/en-US/Blackstone_Careers?q=software&locations=ef375a2335bb0179f899e5065e1fbf2b&locations=ef375a2335bb01d5993383065e1f382b&locations=a5c23e07d3f9100110afed551bed0000&locations=ef375a2335bb01f2aacb0a075e1ff62b&locations=9d4c631a9cd501ef51ff910af90138e3': 'Blackstone',
    'https://nascar.wd1.myworkdayjobs.com/NASCAR?q=software': 'NASCAR',
    'https://groupon.wd5.myworkdayjobs.com/jobs?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'Groupon',
    'https://draftkings.wd1.myworkdayjobs.com/DraftKings/?q=software&locations=5d420c3cf223010162073156e0fe0000&locations=774d00257d2b01b8e5a5b6e63907b173&locations=d98158ef54771000ac2125581ecb0000&locations=5d420c3cf22301016206eda074050000&locations=5d420c3cf22301016206d56bc4110000&locations=774d00257d2b01cf6b7a9c273a077579&locations=5d420c3cf22301016206dd4c41330000&locations=774d00257d2b01a06aeecf273a07f779&locations=36c656617f150101f8f397d9ec130000&locations=774d00257d2b0138c49ae1273a07297a&locations=774d00257d2b0127ed5cbf273a07d979&locations=774d00257d2b01310b60e8273a073d7a&locations=774d00257d2b01cde283aa273a079d79&locations=774d00257d2b01b5b59a95273a076179': 'DraftKings',
    'https://bb.wd3.myworkdayjobs.com/BlackBerry?q=software&locations=a53a14727469107275d89bb164c07ee5&locations=2b810306722301248e863574ef556cbe&locations=c756b1bbadec10e1626403966604cc8d&locations=08618da7938010f7ff7f1b35527f6981&locations=a53a14727469107275d8ab4e1f6d7ef9&locations=c756b1bbadec10e16263e3aaef7ccc54&locations=9d0456a97bd11001eb24c25027fa0000&locations=658dcb07bab7010898b5e489d40b93a3&locations=a53a14727469107275d8d988c7087f35&locations=08618da7938010f7fcc05d29cd68570f&locations=e5a8858f9f8510a48362eb70361ca5cf&locations=08618da7938010f7fa221eb185a54813': 'BlackBerry',
    'https://guidehouse.wd1.myworkdayjobs.com/en-US/External?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'Guidehouse',
    'https://salesforce.wd12.myworkdayjobs.com/en-US/External_Career_Site?q=software&locations=1038e944b1101012453c3c21cd850000&locations=27cc52fb221f1012453a6392417f0000&locations=1038e944b1101012453b2570616b0000&locations=1038e944b1101012453e88646a9a0000&locations=1038e944b11010124540c3b8ffe80000&locations=1038e944b1101012453b30da001a0000&locations=1038e944b1101012453edf70c4ef0000&locations=837ce96d41ed1003d810709470e50000&locations=1038e944b1101012453f1ca83d0a0000&locations=1038e944b11010124539fe8ad1340000&locations=1038e944b1101012453b1104bc1b0000&locations=1038e944b1101012453ec204a4ef0000&locations=1038e944b1101012453b89242f400000&locations=1038e944b1101012453ce26572b10000&locations=6d941861e0411012a163f17caddf0000&locations=1038e944b1101012453eb26824540000&locations=1038e944b1101012453fb2ac8e470000&locations=1038e944b1101012453a519010ae0000&locations=1038e944b1101012453cc894946c0000&locations=1038e944b1101012453b7e549d150000&locations=1038e944b1101012453afacdb9690000&locations=a26a2e385bb51001cfab0315f6a20000&locations=1038e944b1101012453bcb4b56f50000&locations=1038e944b110101245402a1aa0900000&locations=1038e944b1101012453f6677d95a0000&locations=1038e944b1101012453ae52d34d90000&locations=1038e944b1101012453ad88c6c8c0000&locations=1038e944b1101012453f52aa5ae90000': 'Salesforce',
    'https://activision.wd1.myworkdayjobs.com/External?q=software&locations=d5b22c2cbd48018c96c971d9589aee90&locations=d5b22c2cbd48019ab86d76d9589af390&locations=d5b22c2cbd4801ad50207bd9589af890&locations=d5b22c2cbd48015aac6e7fd9589afd90&locations=d5b22c2cbd48011470b583d9589a0291&locations=d5b22c2cbd48015b60d088d9589a0791&locations=d5b22c2cbd480121402f8dd9589a0c91&locations=d5b22c2cbd4801e23ebc91d9589a1191&locations=d5b22c2cbd48014cd50f96d9589a1691&locations=d5b22c2cbd4801b0387b9ad9589a1b91&locations=d5b22c2cbd48010c57c79ed9589a2091&locations=d5b22c2cbd4801d45afaa2d9589a2591&locations=d5b22c2cbd48013f4857a7d9589a2a91&locations=d5b22c2cbd48017aecffabd9589a2f91&locations=d5b22c2cbd4801f2f17ab0d9589a3491&locations=15b06df4e602015bbb324c00c2031c85&locations=15b06df4e60201e356005200c2032185&locations=15b06df4e602015ded8da300c2037185&locations=d5b22c2cbd4801c239802601489a1878&locations=d16fe844933c1001a86eb82286fe0000&locationCountry=bc33aa3152ec42d4995f4791a106ed09': 'Activision',
    'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?locationHierarchy1=2fcb99c455831013ea52fb338f2932d8': 'NVIDIA',
    'https://salesforce.wd12.myworkdayjobs.com/Slack?q=software&CF_-_REC_-_LRV_-_Job_Posting_Anchor_-_Country_from_Job_Posting_Location_Extended=bc33aa3152ec42d4995f4791a106ed09': "Slack",
    'https://walmart.wd5.myworkdayjobs.com/en-US/WalmartExternal?q=software&locationCountry=bc33aa3152ec42d4995f4791a106ed09': "Walmart",
    'https://gapinc.wd1.myworkdayjobs.com/GAPINC': "GAP",
    "https://groupon.wd5.myworkdayjobs.com/jobs": "Groupon"
    }
    
    #    

    
    company_urls = list(company_urls_dict.keys())

    # Add your company URLs here

    for company_url in company_urls:
        if company_url not in job_ids_dict:
            job_ids_dict[company_url] = []

    while True:
        jobs = []
        for company_url in company_urls:
            jobstosend = []
            driver.get(company_url)
            seturl = company_url
            try:
                today = True
                while today:
                    time.sleep(2)
                    wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="css-1q2dra3"]')))
                    
                    job_elements = driver.find_elements(By.XPATH, '//li[@class="css-1q2dra3"]')

                
                    for job_element in job_elements:
                        job_title_element = job_element.find_element(By.XPATH, './/h3/a')
                        job_id_element = job_element.find_element(By.XPATH, './/ul[@data-automation-id="subtitle"]/li')
                        job_id = job_id_element.text
                        posted_on_element = job_element.find_element(By.XPATH, './/dd[@class="css-129m7dg"][preceding-sibling::dt[contains(text(),"posted on")]]')
                        posted_on = posted_on_element.text
                        if '' in posted_on.lower():
                            job_href = job_title_element.get_attribute('href')
                            job_title = job_title_element.text
                            if job_id not in job_ids_dict[company_url]:
                                if "intern" in job_title_element.text.lower():
                                    job_ids_dict[company_url].append(job_id)
                                    jobstosend.append((job_title, job_href))
                                
                            else:
                                print(f"Job ID {job_id} already in job_ids_dict")
                        else:
                            today = False
                    
                    try:
                        next_button = driver.find_element(By.XPATH, '//button[@data-uxi-element-id="next"]')
                    except:
                        break
                    if "disabled" in next_button.get_attribute("class"):
                        break  # exit loop if the "next" button is disabled
                    
                    next_button.click()
            except Exception as e:
                print(f"An error occurred while processing {company_url}: {str(e)}")
                continue

            print(len(job_ids_dict[company_urls[0]]))
            print(len(jobstosend))
            
            

            for job_title, job_href in jobstosend:
                '''driver.get(job_href)
                time.sleep(1)
                
                job_posting_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-automation-id="job-posting-details"]')))
                job_posting_text = job_posting_element.text
                redis_id = str(uuid.uuid4())'''
                job_info = {'company': company_urls_dict[seturl],'role': job_title, 'link': job_href}
                jobs.append(job_info)
                
                
                


        # Write job postings to a CSV file
        with open('job_postings.json', 'w') as f:
            json.dump(jobs, f, indent=4)
            
        break

        # Wait for a certain period before running again
