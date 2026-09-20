import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os, urllib.request

W, H = A4
CREAM = HexColor("#FFF8E7"); SURFACE = HexColor("#FFFEFA"); INK = HexColor("#4B3621"); INK_MUTED = HexColor("#8A6F52")
TAN_DEEP = HexColor("#A66A1C"); HAIRLINE = HexColor("#D8C7A8")

FONT_DIR = "/usr/share/fonts/truetype/nanum"
reg_path = os.path.join(FONT_DIR, "NanumGothic.ttf")
bold_path = os.path.join(FONT_DIR, "NanumGothicBold.ttf")
italic_path = os.path.join(FONT_DIR, "NanumGothic.ttf")
pdfmetrics.registerFont(TTFont("KR", reg_path))
pdfmetrics.registerFont(TTFont("KR-Bold", bold_path))
pdfmetrics.registerFont(TTFont("KR-Italic", italic_path))
kr_prop = fm.FontProperties(fname=reg_path)
kr_bold_prop = fm.FontProperties(fname=bold_path)

REPORT_DATE = "2026.09.20"
REPORT_RANGE = "2026.09.13 - 09.20"
OUT_PDF = "docs/reports/2026-09-20-ice-cream-trends.pdf"
COUNTRIES = [{'key': 'kr', 'name': '한국', 'flavor': '고구마', 'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C', 'headline': '고구마 가을 신제품과 캐릭터 소르베가 이끈 한 주', 'summary_paragraphs': ["9월 셋째 주 한국 아이스크림 시장은 '가을 고구마'를 중심으로 한 제철 디저트 경쟁과 편의점의 캐릭터·비주얼 아이스크림 경쟁이 동시에 벌어졌습니다. 빙그레가 '빵또아 고구마케이크'를 내놓으며 고구마가 이번 시즌 시그니처 재료로 떠올랐고, CU는 산리오 캐릭터(헬로키티·쿠로미) 소르베를, 세븐일레븐은 실제 음식과 구분이 어려운 '하이퍼 리얼리즘' 냉동 디저트를 선보이며 SNS 인증샷 수요를 정조준했습니다. GS25는 프로즌 소르베 라인을 망고·복숭아·레몬으로 확장하며 이미 형성된 화제성을 이어갔습니다.", "배스킨라빈스는 데브시스터즈 '쿠키런' IP와 손잡은 9월 이달의 맛 '초코 퐁당 쿠키런'을 내놓았고, 요아정은 투모로우바이투게더와 협업한 'Pick your TXT' 메뉴로 팬덤층을 겨냥했습니다. SNS에서는 GS25 아이스크림의 품절 대란 인증 게시물과 세븐일레븐 파인애플 아이스크림의 틱톡 리뷰가 잇따라 확산되며 편의점 신상에 대한 소비자 반응을 실시간으로 보여줬습니다. 세븐일레븐은 즉석 스무디 누적 판매 100만 개 돌파를 계기로 냉동 디저트에 이어 사계절 디저트 카테고리 전반을 키우겠다는 전략도 함께 공개했습니다."], 'flavor_bars': [['고구마', 22], ['소르베', 18], ['사과', 15], ['망고', 14], ['초콜릿', 13]], 'pack_bars': [['바 타입', 16], ['하이퍼리얼 모양', 15], ['컵 타입', 14], ['캐릭터 IP', 13], ['포토카드 동봉', 11]], 'content_bars': [['편의점 리뷰 유튜브', 8], ['파인애플 틱톡', 5], ['GS25 소르베 숏츠', 4], ['GS25 품절 게시물', 3], ['산리오 소르베 게시물', 2]], 'refs_intro': '이번 주 한국 리포트는 아래 11개 기사·SNS·영상을 참고해 작성되었습니다.', 'refs': [{'num': 1, 'title': 'CU, 산리오 헬로키티·쿠로미 소르베 출시', 'note': 'CU가 산리오 캐릭터 IP를 활용한 헬로키티(사과맛)·쿠로미(포도맛) 소르베를 각 5,900원에 선보였다. 귀여운 패키지 디자인으로 SNS 소장 인증 게시물이 잇따르고 있다.', 'kind': '신제품', 'thumb_url': None}, {'num': 2, 'title': '세븐일레븐, 계란·파인애플 닮은 하이퍼리얼 디저트 출시', 'note': "세븐일레븐이 실제 계란프라이·파인애플과 구분이 어려운 비주얼의 냉동 디저트 '계란이들었나바'와 '파인애플아이스'를 선보였다. 중국에서 인기였던 단짠 아이스크림을 국내 취향으로 재해석했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 3, 'title': '빙그레, 빵또아 고구마케이크 출시', 'note': "빙그레가 부드러운 카스텔라와 고구마맛 아이스크림을 결합한 '빵또아 고구마케이크'를 출시했다. 고구마맛 쿠키 크럼블을 더해 달고 짭짤한 맛을 구현했으며 빵또아 라인업 4번째 제품이다.", 'kind': '신제품', 'thumb_url': None}, {'num': 4, 'title': 'GS25, 프로즌소르베 망고·복숭아·레몬 라인 확장', 'note': "GS25가 지난해 SNS에서 화제였던 '프로즌 딸기 소르베'에 이어 망고·복숭아·레몬 맛을 추가했다. 과일 원물처럼 정교한 비주얼과 무색소 구성이 특징이다.", 'kind': '신제품', 'thumb_url': None}, {'num': 5, 'title': "배스킨라빈스, 9월 이달의 맛 '초코 퐁당 쿠키런' 공개", 'note': "배스킨라빈스가 데브시스터즈 게임 '쿠키런' IP와 협업한 9월 이달의 맛 '초코 퐁당 쿠키런'을 출시했다. 용감한 쿠키를 모티브로 한 캐러멜·초콜릿 아이스크림 조합이다.", 'kind': '신제품', 'thumb_url': None}, {'num': 6, 'title': '요아정 × 투바투, 포토카드 증정 콜라보 신메뉴', 'note': "요아정이 투모로우바이투게더(TXT)와 협업한 'Pick your TXT' 신메뉴 5종을 선보였다. 구매 시 멤버별 미공개 미니 포토카드를 증정해 팬덤 사이에서 화제를 모으고 있다.", 'kind': '광고', 'thumb_url': None}, {'num': 7, 'title': "GS25 아이스크림 '품절 대란' SNS 인증 게시물 확산", 'note': 'GS25에서 판매하는 아이스크림이 품절 대란을 겪고 있다는 내용의 SNS 게시물이 공유되며 화제를 모으고 있다. 편의점 신상 아이스크림의 높은 수요를 보여주는 사례로 꼽힌다.', 'kind': 'SNS', 'thumb_url': None}, {'num': 8, 'title': "유튜브 '9월 셋째 주 편의점 신제품 리뷰' 인기", 'note': '편의점 신상 리뷰 전문 유튜브 채널이 9월 셋째 주 편의점 신제품(아이스크림 포함)을 소개해 이번 주 편의점 신상 트렌드를 종합적으로 다뤘다.', 'kind': '바이럴', 'thumb_url': 'https://img.youtube.com/vi/_mbUrbdcqEw/hqdefault.jpg'}, {'num': 9, 'title': '세븐일레븐 파인애플 아이스크림 틱톡 리뷰 확산', 'note': "세븐일레븐의 하이퍼리얼리즘 파인애플 모양 아이스크림을 먹어보는 틱톡 리뷰 영상이 확산되며 '진짜 파인애플 같다'는 반응과 함께 가격 논란도 함께 회자되고 있다.", 'kind': '바이럴', 'thumb_url': None}, {'num': 10, 'title': "세븐일레븐, 즉석 스무디로 '사계절 디저트' 카테고리 육성", 'note': '세븐일레븐이 즉석 스무디 누적 판매 100만 개를 넘어서며 여름 한정 음료가 아닌 사계절 디저트로 카테고리를 확장한다고 밝혔다. 말차·ABC스무디 등 가을 신메뉴도 함께 공개했다.', 'kind': '뉴스', 'thumb_url': None}]}, {'key': 'us', 'name': '미국', 'flavor': '호박', 'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C', 'headline': '가을 호박·카라멜 열풍 속 타코벨의 츄러스 아이스크림 타코 화제', 'summary_paragraphs': ["미국 아이스크림 브랜드들이 일제히 가을 시즌에 뛰어들며 데어리퀸·제니스·배스킨라빈스·트레이더조스·페리스·코스트코가 호박·카라멜애플·향신료 중심의 메뉴를 쏟아냈습니다. 가장 화제가 된 것은 타코벨이 솔트앤스트로우와 손잡고 전국 출시한 '츄러스 아이스크림 타코'로, 초코타코의 후속작으로 마케팅되며 다수의 유튜브 시식 영상을 낳았습니다. 배스킨라빈스의 9월 이달의 맛 '비스코프 크렘브륄레'와, 마그넘 바를 크루아상에 끼워 먹는 '크래그넘' 챌린지의 재유행도 SNS 피드를 채웠습니다.", "제니스는 헤이즐넛 스트라차텔라와 미소 버터스카치 브라우니를 앞세운 가을 컬렉션을 LA 매장부터 순차 출시했고, 트레이더조스와 데어리퀸도 각각 애플파이 아이스크림과 신규 블리자드 2종으로 가을 메뉴를 채웠습니다. 코스트코 냉동고에서는 한정판 호박 아이스크림 샌드위치와 베트남 커피 아이스크림이 소비자들 사이에서 화제의 발견으로 공유됐습니다. 마그넘 바를 크루아상에 끼워 먹는 '크래그넘' 챌린지가 다시 유행하며 4주간 810만 회 이상의 조회수를 기록해, 신제품 못지않게 챌린지형 콘텐츠의 화제성이 두드러진 한 주였습니다."], 'flavor_bars': [['호박', 7], ['카라멜', 6], ['비스코프', 4], ['츄러스', 3], ['초콜릿헤이즐넛', 3]], 'pack_bars': [['파인트', 6], ['노벨티 바', 5], ['콘/타코쉘', 3], ['블리자드 컵', 3], ['아이스크림 샌드위치', 2]], 'content_bars': [['마그넘 크래그넘 챌린지', 810], ['츄러스타코 리뷰1', 45], ['츄러스타코 리뷰2', 32], ['두바이초코 틱톡', 28], ['DQ 인스타그램', 12]], 'refs_intro': '이번 주 미국 리포트는 아래 12개 기사·SNS·영상을 참고해 작성되었습니다.', 'refs': [{'num': 1, 'title': "배스킨라빈스, '비스코프 크렘브륄레' 이달의 맛 출시", 'note': "배스킨라빈스가 비스코프 쿠키 조각과 캐러멜 스월을 넣은 커스터드 아이스크림 '비스코프 크렘브륄레'를 9월 1일 전국 출시했다. 쉐이크와 케이크로도 확장했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 2, 'title': "타코벨×솔트앤스트로우, '츄러스 아이스크림 타코' 출시", 'note': "타코벨이 솔트앤스트로우와 협업해 츄러스 아이스크림을 와플콘 '타코'에 채운 신메뉴를 9월 1일 전국 출시했다. 단종된 '초코타코'의 후속작으로 마케팅되며 3.99달러에 판매된다.", 'kind': '신제품', 'thumb_url': None}, {'num': 3, 'title': '제니스, 미소 버터스카치 브라우니 등 가을 컬렉션 출시', 'note': '제니스 스플렌디드 아이스크림이 헤이즐넛 스트라차텔라, 미소 버터스카치 브라우니, 호박 브라운슈거 블론디 등을 담은 가을 컬렉션을 9월 3일 LA 매장부터 순차 출시했다.', 'kind': '신제품', 'thumb_url': None}, {'num': 4, 'title': "트레이더조스, '애플파이 아라모드 아이스크림' 출시", 'note': "트레이더조스가 바닐라 아이스크림에 달콤한 사과와 파이 크러스트 조각을 넣은 '애플파이 아라모드 아이스크림'을 3.99달러에 선보이며 9월 가을 디저트 라인업에 추가했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 5, 'title': '데어리퀸, 가을 블리자드 신메뉴 2종 공개', 'note': "데어리퀸이 '카라멜애플치즈케이크'와 '브라운슈거 쿠키도우' 블리자드를 새로 선보이고, 돌아온 '펌킨파이 블리자드'와 함께 가을 메뉴를 완성했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 6, 'title': "페리스 아이스크림, '프렌드스기빙' 신메뉴 발표", 'note': "페리스 아이스크림이 아몬드 아이스크림에 블랙베리 스월과 슈가쿠키 도우 조각을 넣은 '프렌드스기빙'을 9월 8일 가을 라인업의 일부로 공개했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 7, 'title': '코스트코, 9월 호박 아이스크림 샌드위치·베트남 커피 아이스 화제', 'note': '코스트코 냉동고에서 한정판 호박 아이스크림 샌드위치와 새로 발견된 베트남 커피 아이스크림이 이달의 인기 품목으로 꼽히며 소비자들 사이에서 공유되고 있다.', 'kind': '뉴스', 'thumb_url': None}, {'num': 8, 'title': '유튜버들, 츄러스 아이스크림 타코가 초코타코보다 나은지 시식 리뷰', 'note': '여러 유튜브 채널이 타코벨×솔트앤스트로우 신메뉴를 시식하며 단종된 초코타코와 비교하는 영상을 잇달아 올려 출시 직후 화제성을 키웠다.', 'kind': '바이럴', 'thumb_url': 'https://img.youtube.com/vi/TdevsPI8sQY/hqdefault.jpg'}, {'num': 9, 'title': "마그넘 바를 크루아상에 끼운 '크래그넘' 챌린지 재유행", 'note': "마그넘 바를 속을 파낸 크루아상에 끼워 먹는 '크래그넘' 챌린지가 다시 유행하며 4주간 소셜미디어에서 810만 회 이상의 조회수를 기록했다.", 'kind': '바이럴', 'thumb_url': None}, {'num': 10, 'title': '과일 모양·두바이초콜릿 아이스크림 틱톡 트렌드 확산', 'note': '미시간의 한 디저트 매장에서 만든 과일 모양 아이스크림과 두바이 초콜릿 아이스크림 조각이 여러 크리에이터의 게시물을 통해 틱톡에서 화제를 모으고 있다.', 'kind': 'SNS', 'thumb_url': None}]}, {'key': 'jp', 'name': '일본', 'flavor': '고구마', 'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C', 'headline': '밀고구마와 호지차가 이끈 가을 아이스, PARM 부활 맛이 SNS 강타', 'summary_paragraphs': ["일본 아이스크림 시장에서는 '밀고구마(꿀고구마)'와 호지차 맛이 가을 시즌 신제품을 일제히 장악했습니다. 하겐다즈는 '농밀 고구마' 미니컵을, 세븐일레븐은 '꿀고구마 브륄레' 와플콘을 선보였고, 아카기유업은 가리가리군의 진한 흰 사워맛을 전국 발매했습니다. 가장 큰 화제는 모리나가 'PARM'이 약 5년 만에 부활시킨 호지차 라떼 맛으로, 공식 SNS 게시물이 약 93만 조회수를 기록하며 폭발적인 반응을 얻었습니다. 하겐다즈는 어른을 겨냥한 신규 시리즈 'Classy Night'도 공개하며 브랜딩을 강화했습니다.", "세븐일레븐은 긴자센비키야와 협업한 '와구리 몽블랑'으로 프리미엄 라인을 강화했고, 세븐프리미엄의 피스타치오 초콜릿 바는 주간 랭킹 270위권 밖에서 3위로 급상승하며 눈길을 끌었습니다. 일본 배스킨라빈스(서티원)는 신규 캠페인 '밀키 원더랜드' CM을 예고하며 플레이버 맞히기 퀴즈로 화제를 이어갔고, 로켓뉴스24는 하겐다즈와 무인양품의 고구마 아이스크림을 나란히 비교하는 기사로 가을 감자 아이스 대결 콘텐츠를 만들어냈습니다."], 'flavor_bars': [['고구마', 6], ['호지차', 5], ['카라멜', 5], ['밤·몽블랑', 3], ['피스타치오', 3]], 'pack_bars': [['미니컵', 6], ['바 타입', 5], ['와플콘', 4], ['콘컵', 3], ['박스 세트', 2]], 'content_bars': [['PARM 호지차라떼 게시물', 93], ['하겐다즈x무인양품 기사', 15], ['밀키원더랜드 CM 예고', 12], ['가리가리군 발매 뉴스', 8], ['세븐프리미엄 랭킹 급상승', 6]], 'refs_intro': '이번 주 일본 리포트는 아래 7개 기사·SNS·영상을 참고해 작성되었습니다.', 'refs': [{'num': 1, 'title': "세븐일레븐, '꿀고구마 브륄레' 와플콘 출시", 'note': "세븐일레븐이 세븐프리미엄 라인으로 꿀고구마 크림과 브륄레 캐러멜을 얹은 와플콘 '꿀고구마 브륄레'를 9월 8일 출시했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 2, 'title': "세븐일레븐 × 긴자센비키야, '와구리 몽블랑' 콜라보 출시", 'note': "세븐일레븐이 고급 과일 전문점 긴자센비키야와 협업해 일본산 밤을 몽땅 올린 '마치 와구리 몽블랑'을 9월 15일 선보였다.", 'kind': '신제품', 'thumb_url': None}, {'num': 3, 'title': "하겐다즈, '농밀 고구마' 미니컵 출시", 'note': "하겐다즈가 진한 밀고구마 페이스트를 사용한 미니컵 '농밀 고구마'를 9월 15일 출시하고, 캐러멜 파티 아소트 박스도 함께 선보였다.", 'kind': '신제품', 'thumb_url': None}, {'num': 4, 'title': "아카기유업, '가리가리군 진한 흰 사워' 전국 발매", 'note': "아카기유업이 신맛을 한층 강화한 '가리가리군 진한 흰 사워'를 9월 15일 전국 편의점에 발매하며 정규 라인업을 리뉴얼했다.", 'kind': '신제품', 'thumb_url': None}, {'num': 5, 'title': "모리나가 PARM, 5년 만에 '호지차 라떼' 부활", 'note': "모리나가유업이 'PARM' 브랜드로 약 5년 만에 호지차 라떼 맛을 부활시켰다고 공식 SNS에 공지했으며, 해당 게시물은 약 93만 조회수를 기록하며 폭발적인 반응을 얻었다.", 'kind': '광고', 'thumb_url': None}, {'num': 6, 'title': "일본 배스킨라빈스, '밀키 원더랜드' 신규 CM 예고", 'note': "일본 배스킨라빈스(서티원)가 신규 캠페인 '밀키 원더랜드' CM을 공식 SNS로 예고하며 플레이버 맞히기 퀴즈 이벤트로 화제를 이어가고 있다.", 'kind': '광고', 'thumb_url': None}, {'num': 7, 'title': '세븐프리미엄 피스타치오 초코바, 편의점 랭킹 3위 급상승', 'note': "세븐프리미엄의 '카릿 피스타치오' 초콜릿 바가 주간 편의점 아이스 랭킹에서 270위권 밖에서 3위로 급상승하며 눈길을 끌었다.", 'kind': '뉴스', 'thumb_url': None}, {'num': 8, 'title': '로켓뉴스24, 하겐다즈×무인양품 고구마 아이스 비교기 화제', 'note': '로켓뉴스24가 하겐다즈와 무인양품의 고구마 아이스크림을 나란히 먹어보는 비교 기사를 게재해 가을 감자 아이스 대결 콘텐츠로 독자 사이에서 공유되고 있다.', 'kind': '바이럴', 'thumb_url': None}]}]
OVERVIEW = {'highlights': [('#A66A1C', "한국·일본 모두 '고구마'가 가을 시그니처 맛으로 동시에 떠올랐습니다."), ('#8C3A2E', "타코벨×솔트앤스트로우 '츄러스 타코'가 초코타코 후속작으로 가장 화제를 모았습니다."), ('#5B7F3A', '일본 PARM의 호지차 라떼 부활 게시물이 약 93만 조회수를 기록했습니다.')], 'table_rows': [('한국', '고구마', '5', '2', '고구마·소르베·바타입', '#F3E3D8'), ('미국', '호박', '6', '2', '호박·카라멜·파인트', '#F3E3D8'), ('일본', '고구마', '4', '1', '고구마·미니컵·호지차', '#F3E3D8')], 'analysis': "이번 주는 한국과 일본에서 '고구마(밀고구마)'가 동시에 가을 시그니처 맛으로 떠오른 점이 가장 눈에 띕니다. 두 시장 모두 대형 유통·제조사가 같은 재료를 각기 다른 포맷(빵또아 케이크, 세븐프리미엄 와플콘, 하겐다즈 미니컵)으로 풀어내며 자연스러운 크로스보더 트렌드를 형성했습니다. 미국은 상대적으로 호박·카라멜 등 전통적인 가을 향신료 계열이 강세를 보였고, 타코벨의 '츄러스 아이스크림 타코'처럼 단종 제품의 향수를 자극하는 마케팅이 가장 큰 화제성을 만들어냈습니다. 바이럴 콘텐츠 측면에서는 일본 모리나가 PARM의 호지차 라떼 부활이 약 93만 조회수로 압도적이었고, 미국은 마그넘 '크래그넘' 챌린지가 4주간 810만 조회수를 기록하며 SNS 챌린지형 콘텐츠의 꾸준한 힘을 보여줬습니다. 브랜드 모니터링에서는 세븐일레븐이 한국·일본 양쪽에서 신제품을 동시에 쏟아내며 전주 대비 가장 큰 폭의 언급 증가(+3)를 기록했습니다."}

os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
c = canvas.Canvas(OUT_PDF, pagesize=A4)
TMP = os.path.join(os.path.dirname(OUT_PDF) or ".", "_pdf_tmp")
os.makedirs(TMP, exist_ok=True)

def bg():
    c.setFillColor(CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)

def wrap_text(text, font, size, max_width):
    c.setFont(font, size)
    lines, cur = [], ""
    for ch in text:
        test = cur + ch
        if c.stringWidth(test, font, size) > max_width and cur:
            lines.append(cur); cur = ch
        else:
            cur = test
    if cur: lines.append(cur)
    return lines

def draw_paragraph(text, x, y, max_width, font="KR", size=10, leading=15.5, color=INK):
    c.setFont(font, size); c.setFillColor(color)
    for line in wrap_text(text, font, size, max_width):
        c.drawString(x, y, line); y -= leading
    return y

def draw_box(x, y, w, h, radius=3.5*mm):
    c.setFillColor(SURFACE); c.roundRect(x, y, w, h, radius, fill=1, stroke=0)
    c.setStrokeColor(HAIRLINE); c.setLineWidth(0.6); c.roundRect(x, y, w, h, radius, fill=0, stroke=1)

def draw_boxed_paragraphs(paras, x, y, box_width, font="KR", size=10, leading=15.5, color=INK, pad=6*mm, gap=3*mm):
    all_lines = [wrap_text(p, font, size, box_width - 2*pad) for p in paras]
    total_lines = sum(len(l) for l in all_lines)
    box_h = total_lines*leading + 2*pad + (len(paras)-1)*4*mm
    draw_box(x, y-box_h, box_width, box_h)
    ty = y - pad - size*0.8
    c.setFont(font, size); c.setFillColor(color)
    for lines in all_lines:
        for line in lines:
            c.drawString(x+pad, ty, line); ty -= leading
        ty -= 4*mm
    return y - box_h - gap

def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16)/255 for i in (0,2,4))

def lerp(c1, c2, t):
    return tuple(a+(b-a)*t for a,b in zip(c1,c2))

def draw_tri_gradient(x, y, w, h, hex1, hex2, hex3, steps=140):
    c1_, c2_, c3_ = hexrgb(hex1), hexrgb(hex2), hexrgb(hex3)
    sw = w/steps
    for i in range(steps):
        t = i/(steps-1)
        col = lerp(c1_, c2_, t/0.5) if t < 0.5 else lerp(c2_, c3_, (t-0.5)/0.5)
        c.setFillColorRGB(*col); c.rect(x+i*sw, y, sw+0.6, h, fill=1, stroke=0)

def download_thumb(url, dest):
    try:
        urllib.request.urlretrieve(url, dest)
        return dest
    except Exception:
        return None

def draw_thumb_or_placeholder(x, y, size, url, kind_label, accent_hex):
    path = None
    if url:
        path = download_thumb(url, os.path.join(TMP, f"thumb_{abs(hash(url))}.jpg"))
    if path and os.path.exists(path):
        try:
            c.drawImage(path, x, y, width=size, height=size, mask='auto', preserveAspectRatio=True, anchor='c')
            return
        except Exception:
            pass
    c.setFillColor(HexColor(accent_hex))
    c.roundRect(x, y, size, size, 2*mm, fill=1, stroke=0)
    c.setFont("KR-Bold", 8); c.setFillColor(SURFACE)
    c.drawCentredString(x+size/2, y+size/2-3, kind_label)

def make_bar_chart(path, labels, values, color, title):
    fig, ax = plt.subplots(figsize=(3.1, 2.0), dpi=200)
    ypos = list(range(len(labels)))
    ax.barh(ypos[::-1], values, color=color, height=0.55)
    ax.set_yticks(ypos[::-1]); ax.set_yticklabels(labels, fontproperties=kr_prop, fontsize=8)
    ax.set_title(title, fontproperties=kr_bold_prop, fontsize=9, loc="left", color="#4B3621")
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#D8C7A8")
    ax.tick_params(colors="#4B3621", labelsize=7.5); ax.set_xticks([])
    for i, v in enumerate(values[::-1]):
        ax.text(v+max(values)*0.02, i, str(v), va="center", fontsize=7.5, color="#4B3621")
    fig.tight_layout(); fig.savefig(path, transparent=True); plt.close(fig)

margin = 14*mm

bg()
fx0, fy0, fx1, fy1 = margin, margin, W-margin, H-margin
c.setStrokeColor(INK); c.setLineWidth(1.4); c.rect(fx0, fy0, fx1-fx0, fy1-fy0, fill=0, stroke=1)
c.setLineWidth(0.5); c.rect(fx0+3*mm, fy0+3*mm, fx1-fx0-6*mm, fy1-fy0-6*mm, fill=0, stroke=1)

c.setFont("KR-Italic", 12); c.setFillColor(INK_MUTED)
c.drawCentredString(W/2, H-58*mm, "SCOOP REPORT")
c.drawCentredString(W/2, H-65*mm, "Weekly Ice Cream Intelligence")

c.setFont("KR-Bold", 40); c.setFillColor(INK)
c.drawCentredString(W/2, H-100*mm, "아이스크림")
c.drawCentredString(W/2, H-116*mm, "트렌드 리포트")

c.setFont("KR", 11); c.setFillColor(INK_MUTED)
c.drawCentredString(W/2, H-132*mm, f"{REPORT_DATE}  ·  한국 · 미국 · 일본 3개 시장 종합")

band_h = 46*mm
mids = [ctry["mid"] for ctry in COUNTRIES] + ["#B7CE8C", "#C98A7C"]
draw_tri_gradient(fx0+3*mm, fy0+3*mm, fx1-fx0-6*mm, band_h, mids[0], mids[1], mids[2])
cx, cy = W/2, fy0+3*mm+band_h/2
c.setFillColor(SURFACE); c.circle(cx, cy, 13*mm, fill=1, stroke=0)
c.setFillColor(TAN_DEEP); c.circle(cx, cy-2*mm, 5.2*mm, fill=1, stroke=0)
p = c.beginPath(); p.moveTo(cx-4.2*mm, cy-1*mm); p.lineTo(cx+4.2*mm, cy-1*mm); p.lineTo(cx, cy-11*mm); p.close()
c.drawPath(p, fill=1, stroke=0)
c.showPage()

bg()
top = H-20*mm
c.setFont("KR-Bold", 10); c.setFillColor(INK_MUTED)
c.drawString(margin, top, "SCOOP REPORT"); c.drawRightString(W-margin, top, "02")
c.setStrokeColor(HAIRLINE); c.line(margin, top-4*mm, W-margin, top-4*mm)

y = top-16*mm
colw = (W-2*margin-10*mm)/2
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(margin, y, "리포트 정보")
info_rows = [("리포트","주간 아이스크림 트렌드"), ("기간",REPORT_RANGE), ("발행일",f"{REPORT_DATE} (일)"), ("작성","Scoop Report 자동 리서치")]
box1_top = y-6*mm
box1_h = len(info_rows)*7*mm + 8*mm
draw_box(margin, box1_top-box1_h, colw, box1_h)
y2 = box1_top-6*mm
for label, val in info_rows:
    c.setFont("KR", 9); c.setFillColor(INK_MUTED); c.drawString(margin+5*mm, y2, label)
    c.setFont("KR", 9.5); c.setFillColor(INK); c.drawString(margin+27*mm, y2, val)
    y2 -= 7*mm

x2 = margin+colw+10*mm
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(x2, y, "이번 주 하이라이트")
box2_h = len(OVERVIEW["highlights"])*12*mm + 6*mm
draw_box(x2, box1_top-box2_h, colw, box2_h)
yy = box1_top-9*mm
for col, text in OVERVIEW["highlights"]:
    c.setFillColor(HexColor(col)); c.circle(x2+6.2*mm, yy+1.2*mm, 1.2*mm, fill=1, stroke=0)
    c.setFont("KR", 9.3); c.setFillColor(INK)
    for i, line in enumerate(wrap_text(text, "KR", 9.3, colw-14*mm)):
        c.drawString(x2+10*mm, yy-i*5.2*mm, line)
    yy -= 12*mm

y = box1_top-box1_h-12*mm
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(margin, y, "국가별 요약 대시보드"); y -= 6*mm
headers = ["국가","시그니처 맛","신제품","바이럴","Top 키워드"]
colws = [22*mm, 34*mm, 20*mm, 20*mm, 60*mm]
draw_tri_gradient(margin, y-7*mm, sum(colws), 7*mm, COUNTRIES[0]["deep"], "#7E9A4E", "#8C3A2E")
cx0 = margin
c.setFont("KR-Bold", 9); c.setFillColor(SURFACE)
for h, w in zip(headers, colws):
    c.drawString(cx0+3*mm, y-5*mm, h); cx0 += w
ry = y-7*mm
for name, flavor, new, viral, kw, soft in OVERVIEW["table_rows"]:
    c.setFillColor(HexColor(soft)); c.rect(margin, ry-8*mm, sum(colws), 8*mm, fill=1, stroke=0)
    cx0 = margin
    for v, w in zip([name, flavor, new, viral, kw], colws):
        c.setFont("KR", 9); c.setFillColor(INK); c.drawString(cx0+3*mm, ry-5.5*mm, v); cx0 += w
    ry -= 8*mm
c.setStrokeColor(HAIRLINE); c.setLineWidth(0.6)
c.roundRect(margin, ry, sum(colws), (y-7*mm)-ry+7*mm, 3.5*mm, fill=0, stroke=1)

y = ry-12*mm
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(margin, y, "종합 분석"); y -= 7*mm
draw_boxed_paragraphs([OVERVIEW["analysis"]], margin, y, W-2*margin, size=9.8, leading=15.5)
c.showPage()

page_num = 3
for ctry in COUNTRIES:
    bg()
    top = H-20*mm
    c.setFont("KR-Bold", 10); c.setFillColor(INK_MUTED)
    c.drawString(margin, top, f"SCOOP REPORT · {ctry['name']}"); c.drawRightString(W-margin, top, f"{page_num:02d}")
    c.setStrokeColor(HAIRLINE); c.line(margin, top-4*mm, W-margin, top-4*mm)

    y = top-14*mm
    c.setFillColor(HexColor(ctry["soft"])); c.rect(margin, y-16*mm, W-2*margin, 16*mm, fill=1, stroke=0)
    c.setFont("KR-Bold", 9); c.setFillColor(HexColor(ctry["deep"]))
    c.drawString(margin+6*mm, y-6*mm, f"이주의 시그니처 · {ctry['flavor']}")
    c.setFont("KR-Bold", 15); c.setFillColor(INK)
    c.drawString(margin+6*mm, y-13*mm, ctry["headline"])

    y -= 22*mm
    y = draw_boxed_paragraphs(ctry["summary_paragraphs"], margin, y, W-2*margin, size=10, leading=15.5)

    y -= 4*mm
    c.setFont("KR-Bold", 10.5); c.setFillColor(INK); c.drawString(margin, y, "차트로 보는 이번 주"); y -= 6*mm
    f1 = os.path.join(TMP, f"{ctry['key']}_c1.png"); f2 = os.path.join(TMP, f"{ctry['key']}_c2.png"); f3 = os.path.join(TMP, f"{ctry['key']}_c3.png")
    fl = [x[0] for x in ctry["flavor_bars"]]; fv = [x[1] for x in ctry["flavor_bars"]]
    pl = [x[0] for x in ctry["pack_bars"]]; pv = [x[1] for x in ctry["pack_bars"]]
    cl = [x[0] for x in ctry["content_bars"]]; cvv = [x[1] for x in ctry["content_bars"]]
    make_bar_chart(f1, fl, fv, ctry["deep"], "맛(Flavor) Top 5")
    make_bar_chart(f2, pl, pv, ctry["mid"], "패키징 Top 5")
    make_bar_chart(f3, cl, cvv, ctry["deep"], "콘텐츠별 조회/추천수(만)")
    chart_w = (W-2*margin-2*8*mm-2*6*mm)/3; img_h = chart_w*0.65
    chart_box_h = img_h + 12*mm
    draw_box(margin, y-chart_box_h, W-2*margin, chart_box_h)
    for i, img in enumerate([f1, f2, f3]):
        cxp = margin+6*mm+i*(chart_w+8*mm)
        c.drawImage(img, cxp, y-6*mm-img_h, width=chart_w, height=img_h, mask='auto')
    y -= chart_box_h+10*mm

    c.setFont("KR-Bold", 10.5); c.setFillColor(INK); c.drawString(margin, y, "참고자료 분석"); y -= 6*mm
    thumb_sz = 16*mm; pad = 6*mm
    intro_lines = wrap_text(ctry["refs_intro"], "KR", 9, W-2*margin-2*pad)
    refs_box_h = len(intro_lines)*13 + 5*mm + len(ctry["refs"])*(thumb_sz+5*mm) + 2*pad
    draw_box(margin, y-refs_box_h, W-2*margin, refs_box_h)
    y -= pad
    c.setFont("KR", 9); c.setFillColor(INK_MUTED)
    for line in intro_lines:
        c.drawString(margin+pad, y-8, line); y -= 13
    y -= 5*mm
    for ref in ctry["refs"]:
        row_top = y
        draw_thumb_or_placeholder(margin+pad, row_top-thumb_sz+2, thumb_sz, ref["thumb_url"], ref["kind"], ctry["deep"])
        tx0 = margin+pad+thumb_sz+4*mm
        c.setFont("KR-Bold", 9); c.setFillColor(INK)
        c.drawString(tx0, row_top, f"{ref['num']}.  {ref['title']}")
        ny = draw_paragraph(ref["note"], tx0, row_top-5*mm, W-margin-pad-tx0, size=8.5, leading=12.5, color=INK_MUTED)
        y = min(ny, row_top-thumb_sz)-5*mm

    c.showPage()
    page_num += 1

c.save()
