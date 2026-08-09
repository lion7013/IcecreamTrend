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

REPORT_DATE = "2026.08.09"
REPORT_RANGE = "2026.08.03 - 08.09"
OUT_PDF = "docs/reports/2026-08-09-ice-cream-trends.pdf"

COUNTRIES = [
    {
        "key": "kr", "name": "한국", "flavor": "브륄레",
        "soft": "#F3E3D8", "mid": "#D9A26B", "deep": "#A66A1C",
        "headline": "역대급 폭염에 브륄레·캐릭터 콜라보가 편의점을 휩쓸다",
        "summary_paragraphs": [
            "낮 최고기온이 40도에 육박하는 기록적 폭염이 이어지면서 편의점 아이스크림·얼음컵 매출이 전월 대비 최대 39%까지 뛰었습니다. 배스킨라빈스는 영화 '스머프' 개봉에 맞춰 8월 이달의 맛으로 '블루 바나나 브륄레'를 선보였고, GS25는 유튜버 잠뜰TV의 캐릭터 '픽셀리'와 협업한 빵·아이스크림 시리즈로 출시 한 달 만에 200만 개를 판매했습니다.",
            "넷플릭스 '케이팝 데몬 헌터스' 흥행에 힘입어 GS25의 '소다팝 아이스 브륄레'도 한정판 씰과 함께 1+1 프로모션으로 꾸준히 팔리고 있으며, 빙그레는 목포 RCY 전국캠프에 메로나 등 대표 제품을 후원하는 등 폭염 특수 속 마케팅 경쟁이 뜨겁습니다. 망원시장을 비롯한 곳곳의 품절 후기가 SNS에서 확산되며 이번 여름 소비 트렌드를 상징하는 장면으로 자리잡았습니다.",
        ],
        "flavor_bars": [["브륄레", 6], ["블루바나나", 4], ["멜론", 3], ["소다맛", 3], ["망고", 2]],
        "pack_bars": [["캐릭터 콜라보 패키지", 5], ["미니컵", 4], ["한정판 씰 동봉", 3], ["아이스바/스틱형", 3], ["대용량 파인트", 2]],
        "content_bars": [["픽셀리 콜라보 후기 숏폼", 42], ["블루바나나 브륄레 시식 후기", 28], ["폭염 편의점 냉동간식 브이로그", 19]],
        "refs_intro": "웹검색으로 확인 가능한 로컬 뉴스·유튜브·커뮤니티 게시물을 기준으로 조사했으며, 인스타그램·틱톡 전체 크롤링은 조사 범위에 포함되지 않았습니다.",
        "refs": [
            {"num": 1, "title": "밤낮없는 폭염에 얼음컵 불티…편의점 매출 최대 39% 점프", "note": "뉴스1, 2026-08-08 — 폭염 속 편의점 냉동·냉장 식품 매출 동향", "kind": "기사", "thumb_url": None},
            {"num": 2, "title": "배스킨라빈스, 스머프와 함께한 8월의 맛 '블루 바나나 브륄레' 공개", "note": "뉴스1 — 영화 콜라보 신메뉴 출시 소식", "kind": "기사", "thumb_url": None},
            {"num": 3, "title": "GS25, '픽셀리' 콜라보 빵·아이스크림 출시", "note": "다음뉴스 — 유튜버 캐릭터 협업 신제품 소개", "kind": "기사", "thumb_url": None},
            {"num": 4, "title": "GS25, '픽셀리 시리즈' 출시 한 달 만에 200만 개 판매", "note": "오늘경제 — 판매 실적 보도자료", "kind": "기사", "thumb_url": None},
            {"num": 5, "title": "GS25, 넷플릭스 흥행작 '케이팝 데몬 헌터스'와 K-푸드 컬래버레이션", "note": "브릿지경제 — 소다팝 아이스 브륄레 등 협업 상품 배경", "kind": "기사", "thumb_url": None},
            {"num": 6, "title": "빙그레, '2026년 RCY 전국캠프'에 1억 원·메로나 등 후원", "note": "NSP통신 — 여름 브랜드 마케팅 활동", "kind": "기사", "thumb_url": None},
            {"num": 7, "title": "\"아이스크림 다 나갔어요\"", "note": "네이트뉴스, 2026-07-31 — 폭염 속 품절 현상 스케치", "kind": "기사", "thumb_url": None},
        ],
    },
    {
        "key": "us", "name": "미국", "flavor": "초코",
        "soft": "#EFDDD0", "mid": "#C89173", "deep": "#6B4226",
        "headline": "초콜릿 신제품 러시 속 벤앤제리스, 폭염 특수로 매출 9.2% 급증",
        "summary_paragraphs": [
            "배스킨라빈스는 오레오와 손잡은 한정판 '브루키 배터'를 8월까지 전국 판매하며 브라우니·쿠키 반죽 조합으로 호평을 얻고 있습니다. 벤앤제리스는 쿠키도우, 초콜릿퍼지브라우니, 딸기치즈케이크, 땅콩버터프레첼, 카라멜블론디로 구성된 신규 아이스크림 바 5종을 선보였습니다.",
            "모회사 매그넘아이스크림컴퍼니는 유럽·미주 폭염 특수에 힘입어 2분기 벤앤제리스 매출이 9.2% 성장했다고 밝혔습니다. 한편 맥도날드의 허쉬×M&M 맥플러리는 단종설이 돌았음에도 여전히 판매되며 화제를 모았고, SNS에서는 뉴욕에서 시작된 '버터 아이스크림'이 소프트서브를 녹인 버터에 담가 바삭한 막을 입히는 방식으로 미 전역 베이커리로 퍼지며 바이럴을 일으키고 있습니다.",
        ],
        "flavor_bars": [["초코", 4], ["카라멜", 3], ["쿠키도우", 3], ["버터", 3], ["딸기", 2]],
        "pack_bars": [["파인트", 4], ["아이스크림 바", 4], ["소프트서브/블리자드컵", 2], ["숍인숍 한정 굿즈", 2], ["1+1 프로모션", 2]],
        "content_bars": [["버터 아이스크림 틱톡 트렌드", 85], ["M&M 맥플러리 단종설 논란", 40], ["벤앤제리스 실적 뉴스 화제", 22]],
        "refs_intro": "웹검색으로 확인 가능한 로컬 뉴스·업계 매체·SNS 반응을 기준으로 조사했으며, 인스타그램·틱톡 전체 크롤링은 조사 범위에 포함되지 않았습니다.",
        "refs": [
            {"num": 1, "title": "REVIEW: Baskin-Robbins Brookie Batter Ice Cream", "note": "The Impulsive Buy — 오레오 콜라보 신맛 리뷰", "kind": "기사", "thumb_url": None},
            {"num": 2, "title": "Baskin-Robbins and OREO Brand Serving Up an OREO-Cookie Stacked Summer", "note": "Inspire Brands 공식 발표", "kind": "공식", "thumb_url": None},
            {"num": 3, "title": "Ben & Jerry's unveils new Ice Cream Bars line", "note": "AOL — 신규 바 라인업 소개", "kind": "기사", "thumb_url": None},
            {"num": 4, "title": "Magnum (MICC) Q2 2026 Earnings Call Transcript", "note": "The Motley Fool, 2026-08-05 — 벤앤제리스 2분기 실적 발표", "kind": "기사", "thumb_url": None},
            {"num": 5, "title": "Magnum owner grows sales as acquisitions and Ben & Jerry's fuel first-half gains", "note": "Food Manufacture — 폭염과 매출 성장 배경 분석", "kind": "기사", "thumb_url": None},
            {"num": 6, "title": "Why McDonald's Was Almost Forced To Pull This Iconic McFlurry Flavor", "note": "Tasting Table — M&M 맥플러리 단종설 배경", "kind": "기사", "thumb_url": None},
            {"num": 7, "title": "Butter ice cream: The viral dessert taking TikTok by storm", "note": "Vogue Adria — 버터 아이스크림 바이럴 트렌드", "kind": "기사", "thumb_url": None},
        ],
    },
    {
        "key": "jp", "name": "일본", "flavor": "초코민트",
        "soft": "#F3E3D8", "mid": "#D9A26B", "deep": "#A66A1C",
        "headline": "초코민트 열풍 재점화, 폭염이 사상 최대 아이스 시장을 이끌다",
        "summary_paragraphs": [
            "모리나가유업이 '바리쳬 초코&민트'를 8월 4일 편의점에서 선행 발매하며 초코민트 열풍에 다시 불을 지폈습니다. 스푼으로 초콜릿을 깨먹는 체험형 패키지가 SNS에서 화제를 모았고, '그리운 비엔네타가 떠오른다'는 반응이 다수 이어졌습니다. 업계에서는 초코민트 아이스가 22~24년도 대비 138% 성장하며 올여름 가장 가파른 플레이버로 꼽힌다고 전했습니다.",
            "서티원은 포켓몬 30주년을 기념한 '31포케나츠' 캠페인을 8월 한 달간 전개하며 피카츄 한정 플레이버를 선보였고, 하겐다즈의 '쇼콜라 민트 엑스트라'도 주간 인기 랭킹 상위권을 지키고 있습니다. 기상청 통계상 2025년도 6~8월 평균기온이 평년 대비 2.36도 높아 1898년 관측 이래 가장 더운 여름으로 기록됐으며, 아이스크림 업계는 6년 연속 사상 최대 매출 경신을 이어가고 있습니다.",
        ],
        "flavor_bars": [["초코민트", 6], ["유자", 2], ["땅콩버터", 2], ["파인애플", 2], ["복숭아", 1]],
        "pack_bars": [["체험형(깨먹는) 패키지", 4], ["미니컵", 3], ["콜라보 한정 컵/스티커", 3], ["크리스피샌드", 2], ["축제/이벤트 한정판", 2]],
        "content_bars": [["바리쳬 실식 리뷰 영상", 38], ["31포케나츠 SNS 반응", 25], ["아이파쿠 축제 방문 브이로그", 15]],
        "refs_intro": "웹검색으로 확인 가능한 현지 뉴스·업계 매체·SNS 반응을 기준으로 조사했으며, 인스타그램·틱톡 전체 크롤링은 조사 범위에 포함되지 않았습니다.",
        "refs": [
            {"num": 1, "title": "「Variche（バリッチェ）チョコ＆ミント」8月4日先行発売 8月17日全国発売", "note": "森永乳業 공식 뉴스릴리스", "kind": "공식", "thumb_url": None},
            {"num": 2, "title": "【コンビニ先行】「Variche チョコ＆ミント」を実食！", "note": "Yahoo!ニュース エキスパート — 체험형 식감 리뷰", "kind": "기사", "thumb_url": None},
            {"num": 3, "title": "【2026年8月発売】チョコミントスイーツ新商品まとめ", "note": "えん食べ — 초코민트 신제품 트렌드 정리", "kind": "기사", "thumb_url": None},
            {"num": 4, "title": "サーティワン×ポケモン「31ポケ夏！」8月1日スタート", "note": "東京バーゲンマニア — 포켓몬 30주년 캠페인", "kind": "기사", "thumb_url": None},
            {"num": 5, "title": "ポケモン×サーティワン「31ポケ夏！キャンペーン」開催", "note": "Game Watch — 캠페인 상세", "kind": "기사", "thumb_url": None},
            {"num": 6, "title": "ハーゲンダッツ 週間おすすめランキング（2026年7月24日更新）", "note": "mognavi — 쇼콜라 민트 엑스트라 랭킹", "kind": "기사", "thumb_url": None},
            {"num": 7, "title": "アイス市場 6年連続で最高更新 猛暑が追い風", "note": "食品新聞 — 2025年度 판매 실적", "kind": "기사", "thumb_url": None},
            {"num": 8, "title": "「猛暑の夏商戦」実態は 伸びるアイススラリー", "note": "日本経済新聞 — 폭염과 시장 동향 분석", "kind": "기사", "thumb_url": None},
        ],
    },
]

OVERVIEW = {
    "highlights": [
        ("#A66A1C", "한국, 기록적 폭염에 편의점 아이스크림·얼음컵 매출 최대 39% 급증"),
        ("#6B4226", "미국, 벤앤제리스 폭염 특수로 2분기 매출 9.2% 성장"),
        ("#A66A1C", "일본, 초코민트 열풍 재점화 속 아이스 시장 6년 연속 최대 매출"),
    ],
    "table_rows": [
        ("한국", "브륄레", "2", "1", "브륄레·캐릭터 콜라보", "#F3E3D8"),
        ("미국", "초코", "2", "1", "초코·브라우니·버터", "#EFDDD0"),
        ("일본", "초코민트", "1", "1", "초코민트·체험형 패키지", "#F3E3D8"),
    ],
    "analysis": "이번 주는 세 시장 모두 폭염이 소비를 견인하는 공통 흐름 속에서, 각국은 서로 다른 방식으로 아이스크림 대전을 벌였습니다. 한국은 브륄레 트렌드가 배스킨라빈스·GS25의 캐릭터 콜라보와 맞물리며 편의점 채널을 중심으로 확산되고 있고, 미국은 벤앤제리스가 폭염 특수에 힘입어 모회사 매그넘의 2분기 실적을 견인하며 초콜릿·브라우니 계열 신제품이 강세를 보였습니다. 일본은 모리나가 '바리쳬 초코&민트'가 SNS 화제를 일으키며 초코민트 열풍을 재점화했고, 서티원의 포켓몬 30주년 캠페인이 여름 마케팅 경쟁을 뜨겁게 달구고 있습니다. 세 시장 공통적으로 브라운·초콜릿 계열이 강세를 보이는 가운데, 일본은 6년 연속 사상 최대 매출을 경신하며 폭염이 아이스크림 산업 전반의 구조적 성장 동력이 되고 있음을 보여줍니다.",
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
info_rows = [("리포트","주간 아이스크림 트렌드"), ("기간",REPORT_RANGE), ("발행일",f"{REPORT_DATE} (월)"), ("작성","Scoop Report 자동 리서치")]
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
