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

FONT_DIR = "/tmp/claude-0/-home-user-IcecreamTrend/09f326a6-ffeb-5d98-9de9-9aaf35dc9542/scratchpad/fonts"
reg_path = os.path.join(FONT_DIR, "NotoSansKR-Regular.ttf")
bold_path = os.path.join(FONT_DIR, "NotoSansKR-Bold.ttf")
italic_path = os.path.join(FONT_DIR, "NotoSansKR-Regular.ttf")
pdfmetrics.registerFont(TTFont("KR", reg_path))
pdfmetrics.registerFont(TTFont("KR-Bold", bold_path))
pdfmetrics.registerFont(TTFont("KR-Italic", italic_path))
kr_prop = fm.FontProperties(fname=reg_path)
kr_bold_prop = fm.FontProperties(fname=bold_path)

REPORT_DATE = "2026.10.11"
REPORT_RANGE = "2026.10.04 - 10.11"
OUT_PDF = "docs/reports/2026-10-11-ice-cream-trends.pdf"

COUNTRIES = [
    {
        "key": "kr", "name": "한국", "flavor": "말차",
        "soft": "#E8F0DE", "mid": "#A9C98B", "deep": "#5B7F3A",
        "headline": "흑임자인절미 완판 신드롬과 말차 신메뉴가 이끈 한 주",
        "summary_paragraphs": [
            "10월 첫째 주 한국 아이스크림 시장은 배스킨라빈스의 10월 이달의 맛 '몬스터 크런치 쿠키'와 '말차에 바나나'가 공개되며 가을 신맛 경쟁의 신호탄을 쐈습니다. '말차에 바나나'는 배달의민족 단독 메뉴로 선보여 배달 전용 한정판이라는 새로운 유통 전략을 시도했다는 점에서 주목받았습니다. 동시에 배스킨라빈스는 민트초코·블루베리 조합의 할로윈 시즌 한정 메뉴 '마법사의 할로윈'과 '몬스터 할로윈'을 10월 한 달간 판매하며 할로윈 프로모션의 폭을 넓혔습니다.",
            "이번 주 가장 큰 화제를 모은 것은 롯데웰푸드가 tvN 예능 '우주떡집'과 협업해 내놓은 흑임자인절미 찰떡아이스로, 초기 생산분 50만 개가 5일 만에 완판되고 500세트 한정 사전예약도 18시간 만에 매진되는 품절 대란을 일으켰습니다. 빙그레는 대표 상품 멜로나를 멕시코 대형 유통망 소리아나에 입점시키는 해외 확장 소식을 전했고, 세븐일레븐·CU는 가을 시즌 아이스크림 1+1·2+1 프로모션을 이어가며 편의점 아이스크림 경쟁을 지속했습니다.",
        ],
        "flavor_bars": [["말차", 5], ["멜론", 4], ["밤", 3], ["흑임자·인절미", 3], ["민트초코", 2]],
        "pack_bars": [["콜라보", 5], ["이달의 맛·시즌한정", 4], ["배달 전용 한정판", 3], ["디카페인 PB 소프트콘", 2], ["저당·제로 라인", 2]],
        "content_bars": [["찰떡아이스 완판 기사", 8], ["배스킨라빈스 이달의맛 기사", 5], ["멜로나 멕시코 진출 기사", 4], ["할로윈 라인업 기사", 3], ["디카페인 소프트콘 기사", 2]],
        "refs_intro": "이번 주 한국 리포트는 아래 6개 기사·SNS를 참고해 작성되었습니다.",
        "refs": [
            {"num": 1, "title": "롯데웰푸드 흑임자인절미 찰떡아이스, 5일 만에 50만개 완판", "note": "tvN 예능 '우주떡집'과 협업한 찰떡아이스가 초기 생산분 50만 개를 5일 만에 모두 팔았고, 500세트 한정 사전예약도 18시간 만에 매진됐다.", "kind": "바이럴", "thumb_url": None},
            {"num": 2, "title": "배스킨라빈스, 10월 이달의 맛 '말차에 바나나' 배달앱 단독 출시", "note": "소비자 공모전에서 뽑힌 '몬스터 크런치 쿠키'와 '말차에 바나나'를 10월 이달의 맛으로 출시했다. 말차에 바나나는 배달의민족 단독 메뉴로만 판매한다.", "kind": "신제품", "thumb_url": None},
            {"num": 3, "title": "배스킨라빈스, 할로윈 한정 '마법사의 할로윈'·'몬스터 할로윈' 판매 중", "note": "민트초코와 팝핑캔디를 섞은 '마법사의 할로윈', 블루베리·초코볼을 더한 '몬스터 할로윈' 등 할로윈 시즌 한정 메뉴를 10월 한 달간 판매한다.", "kind": "신제품", "thumb_url": None},
            {"num": 4, "title": "빙그레 멜로나, 멕시코 대형 유통망 소리아나 입점 추진", "note": "빙그레의 대표 상품 멜로나가 K-Expo 행사를 계기로 멕시코 대형 유통망 소리아나에 입점할 예정이며, 피스타치오·코코넛·타로 등 현지화 맛도 함께 수출한다.", "kind": "뉴스", "thumb_url": None},
            {"num": 5, "title": "세븐일레븐, PB 디카페인 소프트콘 '세븐셀렉트 바닐라라떼콘' 꾸준한 인기", "note": "유지방 6%의 디카페인 프리미엄 소프트콘이 카페인에 민감한 소비자층을 중심으로 꾸준한 판매를 이어가고 있다.", "kind": "뉴스", "thumb_url": None},
            {"num": 6, "title": "CU·세븐일레븨, 가을 시즌 아이스크림 1+1·2+1 프로모션 진행", "note": "CU와 세븐일레븨이 각각 멜로나·쿠키앤크림 바 등 인기 아이스크림을 대상으로 1+1·2+1 가을 프로모션을 이어가고 있다.", "kind": "뉴스", "thumb_url": None},
        ],
    },
    {
        "key": "us", "name": "미국", "flavor": "바닐라",
        "soft": "#FFFBEF", "mid": "#F3E3B8", "deep": "#B8912A",
        "headline": "도토리 아이스크림과 츄러스 타코가 이끈 미국의 가을",
        "summary_paragraphs": [
            "10월 첫째 주 미국 아이스크림 시장에서는 전통적인 호박·향신료 가을 맛 대신 색다른 시도가 눈에 띄었습니다. 제니스는 오하이오산 도토리를 직접 채집해 5년간 개발한 '애팔래치안 도토리 파이'를 선보이며 헤이즐넛과 밤을 닮은 독특한 풍미로 화제를 모았습니다. 타코벨은 솔트앤스트로우와 협업한 '츄러스 아이스크림 타코'를 전국 출시해 단종된 초코타코의 후속작이라는 마케팅으로 꾸준한 관심을 받고 있습니다.",
            "콜드스톤은 호박을 뺀 이색 가을 신메뉴 '크럼 앤 겟 잇'을, 데어리퀸은 카라멜애플치즈케이크·브라운슈거쿠키도우 블리자드 2종을 각각 11월까지 선보이며 가을 메뉴 경쟁에 동참했습니다. 음료 업계에서는 큐리그 닥터페퍼가 2027년 출시될 바닐라 베이스의 '아이스크림 플로트' 맛을 예고해 눈길을 끌었고, 업계 전반적으로는 펌킨스파이스 검색 관심도가 전년 대비 크게 줄어든 반면 프로즌요거트 검색 관심도는 2018년 이후 최고치를 기록하며 가벼운 디저트로 소비자 관심이 이동하는 신호도 포착됐습니다.",
        ],
        "flavor_bars": [["바닐라", 6], ["호박", 5], ["카라멜", 4], ["요거트", 3], ["도토리", 2]],
        "pack_bars": [["한정판/리미티드", 6], ["노벨티바·멀티팩", 4], ["파인트", 3], ["하프갤런", 2], ["미니컵", 2]],
        "content_bars": [["에디스 36시간 방치 영상", 25], ["도토리 아이스크림 기사 공유", 8], ["츄러스타코 리뷰 콘텐츠", 6], ["닥터페퍼 플로트 발표 기사", 5], ["프로즌요거트 트렌드 기사", 3]],
        "refs_intro": "이번 주 미국 리포트는 아래 8개 기사·영상을 참고해 작성되었습니다.",
        "refs": [
            {"num": 1, "title": "제니스, 5년 개발한 도토리 아이스크림 '애팔래치안 도토리 파이' 출시", "note": "오하이오산 도토리를 직접 채집해 제분한 재료로 5년간 개발한 신제품을 한정 수량으로 출시했다. 헤이즐넛·밤을 닮은 독특한 풍미가 특징이다.", "kind": "신제품", "thumb_url": None},
            {"num": 2, "title": "큐리그 닥터페퍼, 2027년 출시할 '아이스크림 플로트' 맛 예고", "note": "바닐라 아이스크림 플로트에서 착안한 카라멜·버터스카치 노트의 신맛을 2027년 캔·병 상시 판매 라인으로 출시할 계획을 밝혔다.", "kind": "신제품", "thumb_url": None},
            {"num": 3, "title": "타코벨×솔트앤스트로우 '츄러스 아이스크림 타코' 전국 출시, 꾸준한 화제", "note": "단종된 '초코타코'의 후속작으로 마케팅되며 전국 출시 이후에도 리뷰 콘텐츠가 꾸준히 이어지고 있다.", "kind": "신제품", "thumb_url": None},
            {"num": 4, "title": "콜드스톤, 호박 없는 가을 신메뉴 '크럼 앤 겟 잇' 공개", "note": "그래함크래커 아이스크림에 쿠키도우와 쿠키버터를 섞은 신메뉴가 호박을 뺀 이색 가을 컬렉션으로 11월 17일까지 판매된다.", "kind": "신제품", "thumb_url": None},
            {"num": 5, "title": "데어리퀸, 가을 블리자드 신메뉴 2종 공개", "note": "'카라멜애플치즈케이크'와 '브라운슈거쿠키도우' 블리자드를 새로 선보이고, 돌아온 '펌킨파이 블리자드'와 함께 가을 메뉴를 완성했다.", "kind": "신제품", "thumb_url": None},
            {"num": 6, "title": "미국 '펌킨스파이스' 검색 관심도, 전년 대비 큰 폭 감소", "note": "펌킨스파이스 라떼 검색이 지배적인 주가 올해 3개 주에 그쳐 지난해 32개, 2024년 48개에서 크게 줄었다는 분석이 나왔다.", "kind": "뉴스", "thumb_url": None},
            {"num": 7, "title": "'에디스 아이스크림 36시간 방치' 영상, 품질 논란 재조명", "note": "냉동고 밖에 36시간 둬도 제대로 녹지 않았다는 영상이 25만 회 이상 조회되며 확산되고 있다.", "kind": "바이럴", "thumb_url": None},
            {"num": 8, "title": "미국 프로즌요거트 검색 관심도, 2018년 이후 최고치", "note": "국제프로즌요거트협회 조사에 따르면 검색 관심도가 2018년 7월 이후 최고치를 기록하며 소비자 관심 이동의 신호로 해석된다.", "kind": "뉴스", "thumb_url": None},
        ],
    },
    {
        "key": "jp", "name": "일본", "flavor": "초코",
        "soft": "#EFDDD0", "mid": "#C89173", "deep": "#6B4226",
        "headline": "캐러멜·초콜릿이 이끈 일본의 '어른 입맛' 가을 신제품",
        "summary_paragraphs": [
            "10월 첫째 주 일본 아이스크림 시장은 캐러멜과 초콜릿을 앞세운 '어른 취향' 가을 신제품이 두드러졌습니다. 세븐일레븐은 '마카롱 아이스 캐러멜'과 쌉쌀한 '어른스러운 비터캐러멜 아이스'를 수량 한정으로 출시했고, 하겐다즈는 럼 함량을 높인 '농밀 럼레이즌' 미니컵을 리뉴얼하며 성인 소비자를 겨냥했습니다. 하겐다즈는 한발 더 나가 금박·은박을 더한 리큐어 초콜릿 등 완전히 새로운 어른 전용 라인 'Classy Night'까지 공개하며 브랜딩을 강화했습니다.",
            "할로윈 시즌에는 일본 배스킨라빈스(서티원)가 흑묘 테마 캠페인을 공개하고 뉴욕 브랜드 '팻 위치 뉴욕'과 첫 콜라보 맛 '미스틱 초코스모어'를 선보이며 화제를 모았습니다. 하겐다즈는 훼미리마트와 손잡고 호박 타르트 맛 콜라보도 함께 출시했고, 훼미리마트는 피에르 에르메와 협업한 캐러멜&바닐라 '앙솔로지' 아이스도 선보였습니다. 이무라야는 '야와모치 아이스의 날'(10월 10일)에 맞춰 도라에몽과의 첫 콜라보를 공개하며 브랜드 인지도를 끌어올렸습니다.",
        ],
        "flavor_bars": [["초코", 6], ["카라멜", 5], ["고구마", 4], ["밤·몽블랑", 3], ["바닐라", 2]],
        "pack_bars": [["콜라보 패키지", 4], ["할로윈 한정 패키지", 3], ["수량한정", 3], ["미니컵", 2], ["와플콘", 1]],
        "content_bars": [["도라에몽 콜라보 발표 기사", 10], ["할로윈 캠페인·콜라보 기사", 7], ["클래시나이트 신규 라인 기사", 5], ["펌킨타르트 콜라보 기사", 4], ["럼레이즌 리뉴얼 기사", 3]],
        "refs_intro": "이번 주 일본 리포트는 아래 7개 기사를 참고해 작성되었습니다.",
        "refs": [
            {"num": 1, "title": "세븐일레븨 재팬, '마카롱 아이스 캐러멜'·'어른스러운 비터캐러멜 아이스' 수량한정 출시", "note": "세븐프리미엄 라인에서 마카롱 모양의 캐러멜 아이스와 쌉쌀한 비터캐러멜 아이스를 수량 한정으로 출시했다.", "kind": "신제품", "thumb_url": None},
            {"num": 2, "title": "하겐다즈 재팬, 럼 함량 높인 '농밀 럼레이즌' 미니컵 리뉴얼", "note": "알코올 함량을 약 1.0%로 높인 미니컵을 전국 출시하며 성인 소비자를 겨냥했다.", "kind": "신제품", "thumb_url": None},
            {"num": 3, "title": "하겐다즈×훼미리마트, 할로윈 한정 '파파파판 펌킨타르트' 콜라보 출시", "note": "훼미리마트 단독으로 호박 아이스크림에 호박 쿠키 토핑을 올린 신제품을 출시했다.", "kind": "신제품", "thumb_url": None},
            {"num": 4, "title": "하겐다즈 재팬, 어른 겨냥 신규 라인 'Classy Night' 공개", "note": "금박·은박을 더한 리큐어 초콜릿 맛과 스모키한 너티 캐러멜 맛 2종으로 구성된 신규 라인을 공개했다.", "kind": "신제품", "thumb_url": None},
            {"num": 5, "title": "일본 배스킨라빈스, 할로윈 캠페인서 뉴욕 '팻 위치'와 첫 콜라보", "note": "흑묘 테마 할로윈 캠페인을 통해 뉴욕 브라우니 전문점과 첫 콜라보 맛 '미스틱 초코스모어'를 선보였다.", "kind": "광고", "thumb_url": None},
            {"num": 6, "title": "이무라야, '야와모치 아이스의 날' 기념 도라에몽 첫 콜라보 공개", "note": "일본기념일협회가 공식 지정한 10월 10일에 맞춰 도라에몽과의 첫 캐릭터 콜라보 상품을 공개했다.", "kind": "뉴스", "thumb_url": None},
            {"num": 7, "title": "훼미리마트×피에르 에르메, 캐러멜&바닐라 '앙솔로지' 아이스 콜라보", "note": "프랑스 파티셰 피에르 에르메와 협업해 캐러멜과 바닐라를 조합한 신제품을 10월 신상 라인업에 포함시켰다.", "kind": "신제품", "thumb_url": None},
        ],
    },
]

OVERVIEW = {
    "highlights": [
        ("#5B7F3A", "한국 배스킨라빈스의 '말차에 바나나'가 배달앱 단독 메뉴로 출시됐습니다."),
        ("#8C3A2E", "롯데웰푸드 흑임자인절미 찰떡아이스가 5일 만에 50만 개 완판되며 가장 큰 화제를 모았습니다."),
        ("#6B4226", "일본에서는 하겐다즈·세븐일레븨이 캐러멜 중심의 '어른 입맛' 가을 신제품을 동시에 쏟아냈습니다."),
    ],
    "table_rows": [
        ("한국", "말차", "2", "1", "말차·흑임자인절미·콜라보", "#E8F0DE"),
        ("미국", "바닐라", "5", "1", "바닐라·호박·한정판", "#FFFBEF"),
        ("일본", "초코", "5", "0", "초코·콜라보·카라멜", "#EFDDD0"),
    ],
    "analysis": "이번 주는 세 시장 모두 '어른 취향'과 '콜라보'가 공통 키워드로 떠올랐습니다. 한국에서는 롯데웰푸드의 흑임자인절미 찰떡아이스가 5일 만에 50만 개 완판되며 단일 신제품으로는 가장 큰 화제성을 보였고, 일본에서는 하겐다즈·세븐일레븨이 캐러멜과 럼레이즌을 앞세운 성인 타깃 라인업을 대거 쏟아내며 온 가족보다 어른 소비자를 겨냥했습니다. 미국은 상대적으로 전통적인 호박·향신료 대신 제니스의 '도토리 아이스크림'처럼 실험적인 로컬 재료를 쓰는 시도가 눈에 띄었고, 타코벨×솔트앤스트로우의 '츄러스 타코'는 단종 제품의 향수를 자극하는 마케팅으로 꾸준한 화제를 모았습니다. 브랜드 모니터링에서는 배스킨라빈스가 한국·일본 양쪽에서 신제품과 캠페인을 동시에 전개하며 가장 폭넓은 활동을 보였고, 빙그레는 멜로나의 멕시코 진출로 이번 주 새롭게 모니터링 대상에 올랐습니다.",
}


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
