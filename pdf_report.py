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

FONT_DIR = '/tmp/claude-0/-home-user-IcecreamTrend/0de43495-bcb4-5864-9e27-67b1096533cc/scratchpad/fonts'
reg_path = os.path.join(FONT_DIR, "NotoSansKR-Regular.ttf")
bold_path = os.path.join(FONT_DIR, "NotoSansKR-Bold.ttf")
italic_path = os.path.join(FONT_DIR, "NotoSansKR-Regular.ttf")
pdfmetrics.registerFont(TTFont("KR", reg_path))
pdfmetrics.registerFont(TTFont("KR-Bold", bold_path))
pdfmetrics.registerFont(TTFont("KR-Italic", italic_path))
kr_prop = fm.FontProperties(fname=reg_path)
kr_bold_prop = fm.FontProperties(fname=bold_path)

REPORT_DATE = '2026.10.18'
REPORT_RANGE = '2026.10.11 - 10.18'
OUT_PDF = 'docs/reports/2026-10-18-ice-cream-trends.pdf'

COUNTRIES = [{'key': 'kr',
  'name': '한국',
  'flavor': '바닐라',
  'soft': '#FFFBEF',
  'mid': '#F3E3B8',
  'deep': '#B8912A',
  'headline': '투썸플레이스 반루엔 가을 티 아이스크림, 한글날 이색 콜라보 눈길',
  'summary_paragraphs': ["이번 주 한국 아이스크림 시장은 '콜라보'가 핵심 키워드로 떠올랐습니다. 투썸플레이스가 운영하는 아이스크림 브랜드 반루엔은 가을 "
                         '시즌에 맞춰 호지차·말차라떼 두 가지 차(茶) 풍미 신제품을 16일 출시하며 기존 얼그레이티 제품과 함께 가을 티 라인업을 '
                         "완성했습니다. 같은 주, 여성용품 브랜드 좋은느낌은 수제 아이스크림 브랜드 녹기 전에와 손잡고 한글날 기념 캠페인 '오늘은 내가 "
                         "좋아하는 느낌으로'를 9일부터 22일까지 진행하며, 우유와 바닐라를 조합한 한정 메뉴 '느낌 좋은 바닐라 맛'을 선보였습니다. "
                         '업종을 넘나드는 이색 조합이 눈길을 끌며 SNS에서도 화제를 모았습니다.',
                         '빙그레는 대표 상품 메로나의 신제품으로 황도(백도보다 단맛이 강한 복숭아) 과육을 넣은 버전을 세븐일레븐 중심으로 선보이며, '
                         "가격은 개당 1,000원으로 책정됐습니다. 한편 올해 상반기 SNS에서 화제였던 레시피 아이디어 '순후추콘'이 실제 편의점 "
                         '제품으로 출시되며 후속 리뷰·숏폼 콘텐츠가 계속 올라오고 있습니다. 특유의 단짠 조합에 호불호가 뚜렷하게 갈리는 반응을 보이며, '
                         '레시피에서 실제 상품으로 이어지는 SNS발 제품화 흐름이 이번 주에도 이어졌습니다.'],
  'flavor_bars': [['바닐라', 3], ['말차', 2], ['호지차', 2], ['복숭아', 2], ['순후추', 1]],
  'pack_bars': [['콜라보 패키지', 3], ['미니컵', 2], ['콘', 2], ['스틱', 1], ['한정판 패키지', 1]],
  'content_bars': [['순후추콘 SNS 화제', 5], ['좋은느낌×녹기전에 콜라보', 4], ['반루엔 신제품 소식', 3], ['메로나 황도 소식', 2]],
  'refs_intro': '이번 주 한국 리포트는 아래 4개 기사·SNS를 참고해 작성되었습니다.',
  'refs': [{'num': 1,
            'title': "투썸플레이스 반루엔, 가을 한정 '호지차'·'말차라떼' 출시",
            'note': '투썸플레이스가 전개하는 아이스크림 브랜드 반루엔이 가을 시즌에 맞춰 호지차·말차라떼 두 가지 차(茶) 풍미 신제품을 16일 출시했다. 기존 '
                    '얼그레이티 제품과 함께 가을 티 라인업을 완성하며 관련 캠페인도 함께 전개한다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 2,
            'title': "유한킴벌리 '좋은느낌', 아이스크림 '녹기 전에'와 한글날 콜라보",
            'note': "여성용품 브랜드 좋은느낌이 수제 아이스크림 브랜드 녹기 전에와 손잡고 한글날 기념 캠페인 '오늘은 내가 좋아하는 느낌으로'를 9일부터 "
                    "22일까지 진행한다. 우유와 바닐라를 조합한 한정 메뉴 '느낌 좋은 바닐라 맛'을 흰색·분홍색 레이어로 선보이며, 매장 방문객에게는 한정판 "
                    '스티커도 함께 증정한다.',
            'kind': '광고',
            'thumb_url': None},
           {'num': 3,
            'title': '빙그레 메로나, 황도 과육 더한 신제품 출시',
            'note': '빙그레가 대표 상품 메로나의 신제품으로 황도(백도보다 단맛이 강한 복숭아) 과육을 넣은 버전을 세븐일레븐 중심으로 선보인다. 가격은 개당 '
                    '1,000원으로, 기존 메로나의 샤베트 식감에 과육의 단맛을 더했다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 4,
            'title': "SNS 유행 레시피 '순후추콘', 실제 제품으로 나와 리뷰 콘텐츠 확산",
            'note': "올해 상반기 SNS에서 화제였던 레시피 아이디어 '순후추콘'이 실제 편의점 제품으로 출시되며 후속 리뷰·숏폼 콘텐츠가 계속 올라오고 있다. "
                    '특유의 단짠 조합에 호불호가 뚜렷하게 갈리는 반응이 특징이다.',
            'kind': 'SNS',
            'thumb_url': None}]},
 {'key': 'us',
  'name': '미국',
  'flavor': '초코',
  'soft': '#EFDDD0',
  'mid': '#C89173',
  'deep': '#6B4226',
  'headline': '마그넘 트러플 바 · 월마트 스파이스드 애플, 미국 가을 간식 경쟁',
  'summary_paragraphs': ['이번 주 미국 아이스크림 시장은 프리미엄 바와 가을 시즌 메뉴 확장이 두드러졌습니다. 마그넘은 다크초콜릿 트러플·베리 '
                         '트러플·더블초콜릿바닐라 트러플 등 초콜릿 중심의 프리미엄 바 3종을 새로 선보이며 냉동고 매대의 트러플 바 경쟁에 합류했습니다. '
                         "월마트는 자체 프리미엄 라인 베터굿즈에 스파이스드 애플파이 아이스크림과 신규 '아이스크림 바이트' 2종을 추가하며 고급 자체브랜드 "
                         '디저트 확장을 이어갔습니다. 알디는 바닐라 아이스크림을 호박 모양(잭오랜턴) 펌킨스파이스 쿠키 두 장 사이에 끼운 신제품을 올 '
                         '가을 15종 규모의 펌킨스파이스 라인업 중 하나로 선보였습니다.',
                         "퍼블릭스는 흑설탕 베이스에 캐러멜과 피칸 프랄린을 더한 '뉴올리언스 캐러멜 프랄린'을 올해 첫 시즌 한정 맛으로 냉동고 매대에 "
                         "올렸습니다. 지난 2월 출시된 디핀도츠 최초의 브랜드 협업 맛인 닥터페퍼맛은 소매점·테마파크·공연장 등에서 '상설 라인업'으로 "
                         '자리 잡아 가을까지도 꾸준히 언급되고 있습니다. 업계 보도에 따르면 올해 펌킨스파이스에 대한 소비자 열기가 식으면서 도어대시 주문 '
                         '데이터 기준 피칸 맛 주문이 전년 대비 28% 늘었고, 사과·메이플·바나나 등으로 가을 메뉴가 다변화되는 추세입니다.'],
  'flavor_bars': [['초콜릿 트러플', 3], ['호박 스파이스', 3], ['캐러멜·피칸', 2], ['애플파이', 2], ['피칸', 2]],
  'pack_bars': [['프리미엄 바', 3], ['샌드위치', 2], ['시즌 한정 패키지', 2], ['파인트', 1], ['아이스크림 바이트', 1]],
  'content_bars': [['펌킨스파이스 피로감 분석', 6],
                   ['디핀도츠×닥터페퍼 화제', 5],
                   ['마그넘 트러플 바 출시', 4],
                   ['퍼블릭스 신맛 출시', 3],
                   ['월마트 베터굿즈 확장', 3]],
  'refs_intro': '이번 주 미국 리포트는 아래 6개 기사를 참고해 작성되었습니다.',
  'refs': [{'num': 1,
            'title': '마그넘, 초콜릿 트러플 콘셉트 바 3종 출시',
            'note': '다크초콜릿 트러플·베리 트러플·더블초콜릿바닐라 트러플 등 초콜릿 중심의 프리미엄 바 3종으로 미국 냉동고 매대의 트러플 바 경쟁에 '
                    '합류했다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 2,
            'title': '월마트 프리미엄 라인 베터굿즈, 스파이스드 애플파이 등 신제품 추가',
            'note': "월마트가 자체 프리미엄 아이스크림 라인 베터굿즈에 스파이스드 애플파이 아이스크림과 신규 '아이스크림 바이트' 2종을 추가하며 고급 "
                    '자체브랜드 디저트 확장을 이어가고 있다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 3,
            'title': '알디, 호박 모양 쿠키의 펌킨스파이스 아이스크림 샌드위치 출시',
            'note': '바닐라 아이스크림을 호박 모양(잭오랜턴) 펌킨스파이스 쿠키 두 장 사이에 끼운 신제품으로, 올 가을 15종 규모의 펌킨스파이스 라인업 중 '
                    '하나로 선보였다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 4,
            'title': "퍼블릭스, 올해 첫 시즌 한정 맛 '뉴올리언스 캐러멜 프랄린' 출시",
            'note': "자체 브랜드 아이스크림 라인에서 흑설탕 베이스에 캐러멜과 피칸 프랄린을 더한 '뉴올리언스 캐러멜 프랄린'을 올해 첫 시즌 한정 맛으로 "
                    '냉동고 매대에 선보였다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 5,
            'title': '디핀도츠×닥터페퍼 콜라보, 전국 상설 라인업으로 자리매김',
            'note': "지난 2월 출시된 디핀도츠 최초의 브랜드 협업 맛인 닥터페퍼맛이 소매점·테마파크·공연장 등에서 '상설 라인업'으로 자리 잡아 가을까지도 "
                    '꾸준히 언급되고 있다.',
            'kind': '뉴스',
            'thumb_url': None},
           {'num': 6,
            'title': "'펌킨스파이스 피로감' 속 피칸·사과 맛 주문 28% 증가",
            'note': '업계 보도에 따르면 올해 펌킨스파이스에 대한 소비자 열기가 식으면서, 도어대시 주문 데이터 기준 피칸 맛 주문이 전년 대비 28% 늘었고 '
                    '사과·메이플·바나나 등으로 가을 메뉴가 다변화되는 추세다.',
            'kind': '뉴스',
            'thumb_url': None}]},
 {'key': 'jp',
  'name': '일본',
  'flavor': '밤',
  'soft': '#F3E3D8',
  'mid': '#D9A26B',
  'deep': '#A66A1C',
  'headline': '밤·몽블랑이 점령한 일본 가을 아이스, 캐러멜도 강세',
  'summary_paragraphs': ["이번 주 일본 아이스크림 시장은 밤·몽블랑이 대세였습니다. 모리나가의 'MOW 이탈리안 몽블랑'이 이탈리아산 마론 페이스트를 "
                         '사용해 9월 중순 출시된 뒤에도 꾸준한 인기를 이어가며 10월 셋째 주 편의점 아이스 랭킹 1위를 차지했습니다. 하겐다즈는 가을 '
                         "한정 '진한 럼레이즌' 미니컵, 훼미리마트 단독 '펌킨 타르트', 어른 취향의 '클래시 나이트' 2종을 동시에 출시하며 가을 "
                         '라인업을 확장했습니다. 클래시 나이트는 양주 향을 입힌 쇼콜라와 스모키한 너티 캐러멜 두 가지로, 각 432엔(세금 포함)에 '
                         '판매됩니다.',
                         "메이지 엣셀 수퍼컵은 아이스크림과 쿠키 양쪽에 모두 캐러멜 원료를 사용한 '코쿠우마 캐러멜'을 5일 전국 출시하며 캐러멜 트렌드에 "
                         '힘을 보탰습니다. 이무라야는 모찌 식감의 아이스 6개 층 전부에 우지 말차를 사용한 파르페형 신제품을 선보이며 가을 말차 트렌드에 '
                         "합류했습니다. 글리코는 '목장 짜기' 라인업을 대상으로 산리오 시나모롤과 첫 콜라보 캠페인을 5일부터 12월 25일까지 진행하며 "
                         '영수증 인증 이벤트를 열었습니다.'],
  'flavor_bars': [['밤·몽블랑', 4], ['캐러멜', 3], ['호박(펌킨)', 2], ['말차', 2], ['럼레이즌', 1]],
  'pack_bars': [['미니컵', 3], ['콜라보 패키지', 2], ['시즌 한정 패키지', 2], ['파르페형(6겹)', 1], ['캐릭터 콜라보 굿즈', 1]],
  'content_bars': [['MOW 몽블랑 랭킹 1위', 8],
                   ['클래시 나이트 화제', 5],
                   ['펌킨 타르트 콜라보', 4],
                   ['시나모롤 캠페인', 3],
                   ['코쿠우마 캐러멜 출시', 2]],
  'refs_intro': '이번 주 일본 리포트는 아래 7개 기사를 참고해 작성되었습니다.',
  'refs': [{'num': 1,
            'title': "하겐다즈, 가을 한정 미니컵 '진한 럼레이즌' 출시",
            'note': '기존 럼레이즌보다 럼 풍미를 강화한 가을 한정 미니컵 아이스가 6일 출시됐다. 가격은 373엔이며 전국 슈퍼·편의점·백화점에서 판매된다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 2,
            'title': "하겐다즈, 훼미리마트 단독 '펌킨 타르트' 출시",
            'note': '호박 아이스크림에 호박 소스와 호박 코팅을 더한 가을 한정 콜라보 상품을 훼미리마트에서만 선보인다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 3,
            'title': "하겐다즈, 어른을 위한 신규 라인 '클래시 나이트' 2종 출시",
            'note': '양주 향을 입힌 쇼콜라와 스모키한 너티 캐러멜, 두 가지 어른 취향 아이스를 각 432엔(세금 포함)에 출시한다. 발매일은 10월 20일로 '
                    '알려졌다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 4,
            'title': "메이지 엣셀 수퍼컵, 캐러멜에 집중한 '코쿠우마 캐러멜' 전국 출시",
            'note': '아이스크림과 쿠키 양쪽에 모두 캐러멜 원료를 사용해 처음부터 끝까지 캐러멜만 느껴지도록 만든 신제품이 5일 전국 출시됐다. 희망소비자가는 '
                    '200ml에 194엔이다.',
            'kind': '신제품',
            'thumb_url': None},
           {'num': 5,
            'title': "모리나가 'MOW 이탈리안 몽블랑', 편의점 아이스 주간 랭킹 1위",
            'note': '이탈리아산 마론 페이스트를 사용한 몽블랑 아이스가 9월 중순 출시된 뒤에도 꾸준한 인기를 이어가며 10월 셋째 주 편의점 아이스 랭킹 '
                    '1위를 차지했다.',
            'kind': '바이럴',
            'thumb_url': None},
           {'num': 6,
            'title': "글리코 '보쿠조시보리', 산리오 시나모롤과 첫 콜라보 캠페인",
            'note': "'목장 짜기' 전 라인업을 대상으로 영수증 인증 응모 시 시나모롤 디자인 상품을 1,000명에게 추첨 증정하는 캠페인을 5일부터 12월 "
                    '25일까지 진행한다.',
            'kind': '광고',
            'thumb_url': None},
           {'num': 7,
            'title': '이무라야, 6개 층 전부가 우지 말차인 파르페형 아이스 출시',
            'note': '모찌 식감의 아이스 6개 층 전부에 우지 말차를 사용한 가을 신제품으로, 10월 신작 아이스 모음에 포함돼 소개됐다.',
            'kind': '신제품',
            'thumb_url': None}]}]

OVERVIEW = {'highlights': [('#A66A1C', "일본 모리나가의 'MOW 이탈리안 몽블랑'이 편의점 아이스 주간 랭킹 1위에 올랐습니다."),
                ('#B8912A', '한국에서는 투썸플레이스 반루엔과 유한킴벌리×녹기 전에의 이색 콜라보가 동시에 화제를 모았습니다.'),
                ('#6B4226', '미국 마그넘이 초콜릿 트러플 바 3종을 새로 출시하며 프리미엄 바 경쟁에 불을 붙였습니다.')],
 'table_rows': [('한국', '바닐라', '2', '0', '티플레이버·콜라보·바닐라', '#FFFBEF'),
                ('미국', '초코', '4', '0', '초콜릿트러플·펌킨스파이스·캐러멜', '#EFDDD0'),
                ('일본', '밤', '5', '1', '밤·몽블랑·캐러멜', '#F3E3D8')],
 'analysis': "이번 주는 세 시장 모두 '콜라보'와 '시즌 한정'이 공통 키워드로 떠올랐습니다. 한국에서는 투썸플레이스 반루엔의 가을 티 신제품과 유한킴벌리×녹기 "
             '전에의 한글날 콜라보처럼 업종을 넘나드는 이색 조합이 눈길을 끌었고, 빙그레 메로나는 황도 과육을 더한 신제품으로 가을 시즌에 대응했습니다. 일본에서는 '
             "모리나가의 'MOW 이탈리안 몽블랑'이 편의점 랭킹 1위를 차지하며 밤·몽블랑 열풍을 입증했고, 하겐다즈·메이지·이무라야가 각각 럼레이즌·캐러멜·말차 "
             '신제품을 동시에 쏟아내며 가을 경쟁이 가장 치열했습니다. 미국은 마그넘의 초콜릿 트러플 바와 월마트·알디·퍼블릭스의 가을 시즌 한정 맛이 이어졌지만, '
             '업계에서는 펌킨스파이스 피로감 속에 피칸·사과 맛 주문이 28% 늘었다는 분석이 나오며 소비자 선호가 조금씩 바뀌고 있음을 보여줬습니다. 브랜드 '
             '모니터링에서는 화이트리스트 4개 브랜드 중 빙그레만 이번 주 언급되며 비교적 조용한 한 주였습니다.'}

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
