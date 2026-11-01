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

REPORT_DATE = "2026.11.01"
REPORT_RANGE = "2026.10.26 - 11.01"
OUT_PDF = "docs/reports/2026-11-01-ice-cream-trends.pdf"
COUNTRIES = [
    {
        "key": "kr", "name": "한국", "flavor": "복숭아",
        "soft": "#FFEFE3", "mid": "#FFC2A1", "deep": "#E2734F",
        "headline": "배스킨라빈스·도라에몽 콜라보, 빙그레 복숭아 신상이 이끈 11월 초",
        "summary_paragraphs": [
            "배스킨라빈스가 도라에몽과 손잡고 팥·슈크림을 결합한 11월 이달의 맛 '팥붕! 슈붕!'과 치토스 밀크쉐이크 아이스크림을 함께 내놨다. 빙그레는 진짜 복숭아를 연상시키는 '메로나 황도'로 복숭아 맛 경쟁에 불을 붙였고, 더위사냥 키위 슬러시와 투게더 블루베리 프로즌요거트까지 라인업을 넓혔다. GS25는 그릭요거트 복숭아맛 쫀득바를 추가해 400만개 판매를 넘긴 '쫀득한 식감' 라인업을 키우는 중이며, 세븐일레븐은 부라보콘 피스타치오 등 1+1·2+1 행사로 가격 경쟁을 이어갔다. 캐릭터 콜라보와 복숭아·팥 등 가을 정서를 겨냥한 맛이 이번 주 핵심 흐름이다.",
            "편의점·제과업체를 가로지르는 이번 주 흐름은 두 가지다. 하나는 배스킨라빈스·도라에몽처럼 캐릭터 IP와의 협업이 화제성을 높이는 공식으로 자리잡고 있다는 점이고, 다른 하나는 그릭요거트·쫀득한 식감처럼 '건강한 듯 쫀득한' 조합이 복숭아 과육과 결합해 가을 신상의 공통 코드가 되고 있다는 점이다. 세븐일레븐의 1+1·2+1 행사는 신제품 출시 못지않게 기존 인기 제품의 반복 구매를 유도하는 가격 전략이 활발하다는 신호로 읽힌다. 다음 주에도 복숭아·팥 계열 신상과 캐릭터 콜라보 소식이 이어질 가능성이 높다.",
        ],
        "flavor_bars": [["복숭아", 6], ["팥", 4], ["요거트(그릭)", 4], ["피스타치오", 3], ["초코", 3]],
        "pack_bars": [["캐릭터 콜라보 패키지", 5], ["쫀득바 라인", 4], ["1+1·2+1 행사", 4], ["파우치형", 3], ["미니컵", 2]],
        "content_bars": [["배스킨라빈스 도라에몽 콜라보 소식", 8], ["빙그레 메로나 황도 공식 SNS", 6], ["GS25 쫀득바 트렌드 기사", 5], ["세븐일레븐 10월 행사 커뮤니티 반응", 4], ["편의점 아이스크림 비교 게시물", 3]],
        "refs_intro": "이번 주 한국 섹션은 배스킨라빈스·빙그레·GS25의 신제품 보도자료와 가격비교 커뮤니티 게시물을 중심으로 조사했다.",
        "refs": [
            {"num": 1, "title": "배스킨라빈스 11월 이달의 맛 '팥붕! 슈붕!' 보도", "note": "도라에몽 콜라보 팥붕슈붕 신메뉴 소식", "kind": "기사", "thumb_url": None},
            {"num": 2, "title": "빙그레 '메로나 황도' 보도", "note": "복숭아 과육 담은 메로나 신제품 소식", "kind": "기사", "thumb_url": None},
            {"num": 3, "title": "GS25 쫀득 아이스크림 라인업 확대 — 청년일보", "note": "그릭요거트 복숭아맛 쫀득바 추가 출시 보도", "kind": "기사", "thumb_url": None},
            {"num": 4, "title": "빙그레 더위사냥 키위 슬러시", "note": "파우치형 키위 슬러시 신제품 소식", "kind": "기사", "thumb_url": None},
            {"num": 5, "title": "빙그레 투게더 프로즌요거트 블루베리", "note": "블루베리 프로즌요거트 신제품 소식", "kind": "기사", "thumb_url": None},
        ],
    },
    {
        "key": "us", "name": "미국", "flavor": "피스타치오",
        "soft": "#EFF3DE", "mid": "#B7CE8C", "deep": "#7E9A4E",
        "headline": "두바이 초콜릿 열풍 탄 피스타치오 아이스크림, 11월 미국 강타",
        "summary_paragraphs": [
            "배스킨라빈스가 두바이 초콜릿 트렌드에서 착안한 '피스타치오 초콜릿 바'를 11월의 맛으로 공개하며 11월을 열었다. 10월엔 '갤럭틱 브라우니'가 유명 스낵케이크를 닮았다는 반응으로 화제를 모았고, 콜드스톤과 하겐다즈도 가을 신메뉴를 잇달아 선보였다. SNS에서는 태국에서 시작된 '크루아상 아이스크림 샌드' 챌린지가 전 세계로 퍼지며 여전히 상위권 화제성을 유지하고 있다. 블루벨 등 중소 브랜드들도 화이트 초콜릿 모카 등 신맛을 꾸준히 내놓으며 경쟁에 합류했다.",
            "브랜드별로는 대형 체인(배스킨라빈스, 콜드스톤, 하겐다즈)이 매달 새 맛을 공식화하는 '이달의 맛' 캘린더 전략을 적극 활용하는 모습이 뚜렷했다. 동시에 SNS 바이럴은 브랜드가 직접 만들지 않은 '해킹형' 레시피(크루아상 샌드, 워터멜론 아이스크림)가 주도하고 있어, 공식 마케팅과 유저 제작 콘텐츠가 별도 트랙으로 화제성을 나눠 갖는 양상이다. 블루벨 같은 중견 브랜드도 신맛을 꾸준히 추가하며 틈새 수요에 대응하고 있다.",
        ],
        "flavor_bars": [["피스타치오", 5], ["브라우니·초코", 4], ["체리", 3], ["바나나", 2], ["허니바닐라", 2]],
        "pack_bars": [["크루아상 샌드", 6], ["바(Bar)", 4], ["파인트", 4], ["쉐이크·선데 세트", 3], ["시즌 한정 패키지", 2]],
        "content_bars": [["Magnum 크루아상 챌린지", 850], ["2가지 재료 워터멜론 아이스크림", 420], ["피스타치오 초콜릿바 리뷰", 150], ["코지 콜렉션 언박싱", 90], ["코스믹 브라우니 비교 리뷰", 75]],
        "refs_intro": "이번 주 미국 섹션은 배스킨라빈스·콜드스톤·하겐다즈 신상 보도와 SNS 바이럴 챌린지 관련 기사를 중심으로 조사했다.",
        "refs": [
            {"num": 1, "title": "Cold Stone's 2026 Fall Flavors", "note": "콜드스톤 가을 신메뉴 '코지 콜렉션' 소식", "kind": "기사", "thumb_url": None},
            {"num": 2, "title": "Little Debbie's Nostalgic Snack Inspired New Baskin-Robbins Flavor", "note": "배스킨라빈스 10월 맛 '갤럭틱 브라우니' 소식", "kind": "기사", "thumb_url": None},
            {"num": 3, "title": "Baskin-Robbins Debuts Dubai Chocolate-Inspired Treats", "note": "두바이 초콜릿 트렌드 반영한 11월 신메뉴 소식", "kind": "기사", "thumb_url": None},
            {"num": 4, "title": "Häagen-Dazs Launches 6 New Ice Cream Flavors", "note": "하겐다즈 신상 6종 출시 소식", "kind": "기사", "thumb_url": None},
            {"num": 5, "title": "The Magnum Croissant Trend", "note": "크루아상 아이스크림 샌드 챌린지 바이럴 소식", "kind": "SNS", "thumb_url": None},
            {"num": 6, "title": "Two-Ingredient Watermelon Ice Cream Becomes Viral TikTok Summer Hit", "note": "2가지 재료 워터멜론 아이스크림 바이럴 소식", "kind": "SNS", "thumb_url": None},
            {"num": 7, "title": "Blue Bell Releases New White Chocolate Mocha Flavor", "note": "블루벨 신상 화이트 초콜릿 모카 소식", "kind": "기사", "thumb_url": None},
        ],
    },
    {
        "key": "jp", "name": "일본", "flavor": "고구마",
        "soft": "#F3E3D8", "mid": "#D9A26B", "deep": "#A66A1C",
        "headline": "일본, 가을 고구마·밤 아이스 신상 경쟁 가속",
        "summary_paragraphs": [
            "이번 주 일본 아이스크림 시장은 가을 시즌 특유의 고구마·밤 풍미 신제품이 주도했다. 세븐일레븐은 '와플콘 밀고구마 브륄레'와 긴자 센비키야와 협업한 '마루데 와구리 몽블랑'을 잇달아 선보이며 편의점 디저트 경쟁에 불을 붙였다. 하겐다즈는 성인 타겟 '클래시 나이트' 시리즈로 양주 향을 더한 쇼콜라와 캐러멜 아이스를 선보여 프리미엄 라인을 강화했다. 롯데웰푸드는 '유키미다이후쿠'의 가을 한정 오츠키미 디자인으로 체험형 이벤트까지 열며 SNS 화제성을 키웠다.",
            "이번 주 일본 시장에서 눈에 띄는 점은 '이번 주 신규 발표'보다 9~10월에 나온 가을 한정 상품들이 여전히 매장과 SNS에서 화제를 이어가고 있다는 것이다. 세븐일레븐·하겐다즈·롯데웰푸드 등 주요 브랜드가 고구마·밤·캐러멜 등 가을 정서의 재료를 공통적으로 채택했고, 가리가리군처럼 동물원 콜라보 이벤트형 마케팅도 꾸준한 화제성을 유지했다. 신제품 발표 주기가 한국·미국보다 느린 편이라, 다음 리포트에서도 유사한 흐름이 이어질 가능성이 있다.",
        ],
        "flavor_bars": [["고구마", 5], ["밤", 4], ["캐러멜", 3], ["럼레이즌", 2], ["쇼콜라", 2]],
        "pack_bars": [["와플콘", 3], ["미니컵", 3], ["다이후쿠(모찌)", 2], ["한정디자인패키지", 2], ["멀티팩", 1]],
        "content_bars": [["가리가리군 x 도부동물공원 콜라보 게시물", 12], ["하겐다즈 클래시나이트 리뷰영상", 9], ["유키미다이후쿠 오츠키미카이 이벤트 브이로그", 7], ["세븐프리미엄 와구리몽블랑 시식 리뷰", 6], ["이모젠느 고구마 아이스 소개 영상", 4]],
        "refs_intro": "이번 주 일본 섹션은 세븐일레븐·하겐다즈·롯데웰푸드 신상 특집과 콜라보 이벤트 관련 자료를 중심으로 조사했다.",
        "refs": [
            {"num": 1, "title": "세븐프리미엄 가을 신상 특집 (와플콘 밀고구마 브륄레 외)", "note": "세븐일레븐 가을 고구마 신상 특집 기사", "kind": "기사", "thumb_url": None},
            {"num": 2, "title": "하겐다즈 10월 신상 '클래시 나이트'·'호죠쿠 럼레이즌'", "note": "하겐다즈 성인 타겟 신상 소식", "kind": "기사", "thumb_url": None},
            {"num": 3, "title": "유키미다이후쿠 가을 한정 '오츠키미 지타테'", "note": "롯데웰푸드 유키미다이후쿠 가을 한정판 소식", "kind": "기사", "thumb_url": None},
            {"num": 4, "title": "유키미다이후쿠 '다같이 오츠키미카이' 이벤트 정보", "note": "신주쿠 체험형 이벤트 정보", "kind": "행사", "thumb_url": None},
            {"num": 5, "title": "세븐일레븐 신상 발매일·가격 정보", "note": "와플콘 밀고구마 브륄레 발매 정보", "kind": "기사", "thumb_url": None},
            {"num": 6, "title": "가리가리군 관련 자료(동물원 콜라보 포함)", "note": "가리가리군 동물원 콜라보 이벤트 소식", "kind": "SNS", "thumb_url": None},
        ],
    },
]
OVERVIEW = {
    "highlights": [
        ("#E2734F", "한국: 배스킨라빈스·도라에몽 콜라보 '팥붕! 슈붕!' 11월 맛 출시"),
        ("#7E9A4E", "미국: 두바이 초콜릿에서 비롯된 피스타치오 아이스크림, 11월 신메뉴로 확산"),
        ("#A66A1C", "일본: 세븐일레븐·하겐다즈 가을 고구마·밤 신상 경쟁"),
    ],
    "table_rows": [
        ("한국", "복숭아", "6", "0", "복숭아", "#FFEFE3"),
        ("미국", "피스타치오", "5", "2", "크루아상 샌드", "#EFF3DE"),
        ("일본", "고구마", "5", "1", "고구마", "#F3E3D8"),
    ],
    "analysis": "이번 주 세 시장을 종합하면, 가을 시즌 특유의 뿌리채소·팥 계열 맛(한국 팥, 일본 고구마·밤)과 전 세계적 바이럴에서 비롯된 견과류 디저트 트렌드(미국 피스타치오·두바이 초콜릿)가 동시에 부상하고 있다. 한국은 캐릭터 IP 콜라보와 그릭요거트·쫀득한 식감이 결합한 신상이 신제품 수를 끌어올렸고, 미국은 SNS에서 출발한 '해킹형' 레시피 바이럴이 공식 신메뉴 발표와 별도로 화제성을 양분했다. 일본은 신제품 발표 주기가 상대적으로 느려 9~10월 출시작이 여전히 화제의 중심에 있었고, 체험형 이벤트·동물원 콜라보 같은 오프라인 마케팅이 두드러졌다. 세 시장 모두 편의점·대형 프랜차이즈가 신상 발표의 중심이라는 공통점을 보였으며, 다음 주에도 가을 정서의 맛과 캐릭터·IP 협업이 핵심 흐름으로 이어질 가능성이 크다.",
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
