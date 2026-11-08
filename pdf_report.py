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

REPORT_DATE = "2026.11.08"
REPORT_RANGE = "2026.11.02 - 11.08"
OUT_PDF = "docs/reports/2026-11-08-ice-cream-trends.pdf"
COUNTRIES = [
    {
        "key": 'kr', "name": '한국', "flavor": '초코',
        "soft": '#EFDDD0', "mid": '#C89173', "deep": '#6B4226',
        "headline": 'GS25 초코바 신상과 배스킨라빈스 가격 인상이 가른 11월 둘째 주',
        "summary_paragraphs": ["이번 주 한국 아이스크림 시장은 초콜릿 맛과 가격 이슈가 동시에 떠올랐다. GS25는 스니커즈·트윅스를 본뜬 초코바 아이스크림과 콜라 맛 '스윗믹스 아이스젤리바', 튀르키예식 카이막을 접목한 '허니모찌 카이막 아이스밀크'를 잇달아 내놓으며 SNS에서 화제를 모았다. CU는 하겐다즈 마카다미아·바닐라·벨지안초콜릿·커피 파인트와 그린티 미니컵을 2+1 행사에 올렸고, 세븐일레븐도 빙그레 부라보바닐라를 1+1로 선보이며 편의점 3사의 가격 경쟁을 이어갔다. 한편 배스킨라빈스는 지난달 12일부터 아이스크림·음료 46종 가격을 평균 5.9% 올려 대표 메뉴 싱글레귤러가 처음으로 4000원을 넘겼다."],
        "flavor_bars": [['초코', 6], ['팥', 4], ['바닐라', 3], ['커피', 3], ['말차', 2]],
        "pack_bars": [['2+1·1+1 행사', 6], ['파인트', 4], ['콜라보 패키지', 3], ['미니컵', 3], ['콘형', 2]],
        "content_bars": [['순후추콘 레시피 유튜브 쇼츠', 109], ['GS25 스니커즈·트윅스 SNS 게시물', 15], ['배스킨라빈스 가격인상 보도', 9], ['빙그레 메로나 해외진출 보도', 6], ['CU 하겐다즈 2+1 커뮤니티 반응', 4]],
        "refs_intro": '이번 주 한국 섹션은 GS25·배스킨라빈스·빙그레의 신제품·가격 보도와 SNS 바이럴 게시물을 중심으로 조사했다.',
        "refs": [{'num': 1, 'title': '배스킨라빈스 46종 가격 5.9% 인상 보도', 'note': '싱글레귤러 4000원 돌파 가격 인상 소식', 'kind': '기사', 'thumb_url': None}, {'num': 2, 'title': 'GS25 신상 2종 및 SNS 화제 정리', 'note': '스윗믹스 아이스젤리바·허니모찌 카이막, 초코바 SNS 반응', 'kind': '기사', 'thumb_url': None}, {'num': 3, 'title': 'CU·세븐일레븐 11월 행사 상품정보', 'note': '하겐다즈 2+1, 부라보바닐라 1+1 행사 정보', 'kind': '기사', 'thumb_url': None}, {'num': 4, 'title': '순후추콘 레시피 바이럴 기사', 'note': '유튜브 쇼츠 109만 회 바이럴 후 실제 제품화', 'kind': 'SNS', 'thumb_url': None}, {'num': 5, 'title': '빙그레 메로나 해외 확장 보도(멕시코·프랑스)', 'note': '소리아나 입점 추진 및 SIAL Paris 신맛 공개 소식', 'kind': '기사', 'thumb_url': None}],
    },
    {
        "key": 'us', "name": '미국', "flavor": '바닐라',
        "soft": '#FFFBEF', "mid": '#F3E3B8', "deep": '#B8912A',
        "headline": '홀리데이 시즌 겨냥한 스틱·샌드위치 신제품이 주도한 미국 11월',
        "summary_paragraphs": ["미국에서는 홀리데이 시즌을 겨냥한 신제품이 이번 주 흐름을 이끌었다. 패트보이는 페퍼민트 아이스크림 샌드위치와 생강빵 맛 샌드위치를 기간 한정으로 출시해 다크초콜릿·그레이엄 웨이퍼로 감쌌다. 콜드스톤 크리머리는 그레이엄 크래커 베이스의 신메뉴 '크럼 앤 겟 잇'을 선보이며 인기 메뉴 '고잉 바나나스 포 젤로 푸딩'과 함께 11월 17일까지 가을 한정 컬렉션으로 판매한다. 벤앤제리스는 숟가락 없이 즐기는 초콜릿 코팅 스틱형 아이스크림 라인을 쿠키도우·초코퍼지브라우니 두 맛으로 확장해 편의점 유통을 늘렸다."],
        "flavor_bars": [['바닐라', 4], ['생강빵', 2], ['페퍼민트', 2], ['초코퍼지브라우니', 1], ['쿠키도우', 1]],
        "pack_bars": [['스틱형', 3], ['샌드위치형', 2], ['기간한정 컬렉션', 2], ['멀티팩(6입)', 1], ['편의점 유통', 1]],
        "content_bars": [['FatBoy 홀리데이 샌드위치 보도', 6], ['콜드스톤 가을 컬렉션 보도', 4], ['벤앤제리스 스틱라인 확장 보도', 3]],
        "refs_intro": '이번 주 미국 섹션은 패트보이·콜드스톤·벤앤제리스의 홀리데이 신메뉴 보도를 중심으로 조사했다.',
        "refs": [{'num': 1, 'title': 'FatBoy Ice Cream Launches Limited Edition Peppermint and Gingerbread Sandwiches', 'note': '패트보이 홀리데이 샌드위치 2종 출시 소식', 'kind': '기사', 'thumb_url': None}, {'num': 2, 'title': "Cold Stone's 2026 Fall Flavors", 'note': '콜드스톤 가을 한정 컬렉션 소식', 'kind': '기사', 'thumb_url': None}, {'num': 3, 'title': "Ben & Jerry's Introduces New Ice Cream Products", 'note': '벤앤제리스 스틱형 라인 확장 소식', 'kind': '기사', 'thumb_url': None}],
    },
    {
        "key": 'jp', "name": '일본', "flavor": '호박',
        "soft": '#F3E3D8', "mid": '#D9A26B', "deep": '#A66A1C',
        "headline": '하겐다즈 호박 타르트, 모그나비 주간 랭킹 1위 지키며 11월 신상 주도',
        "summary_paragraphs": ["하겐다즈 재팬의 패밀리마트 한정 '파파파파판프킨타르트'가 10월 출시 한 달 뒤에도 SNS에서 화제를 이어가며 모그나비 주간 아이스크림 랭킹 1위(11월 6일 기준)를 지켰고, '크레이지 버터' 맛도 241위에서 80위로 급상승했다. 11월 3일에는 하겐다즈가 새 시리즈 '케이크바' 1호 '산딸기 가토 쇼콜라'와 크리스피 샌드 '밤과 카시스 파르페'를 동시 출시하며 가을 디저트 경쟁에 불을 붙였다."],
        "flavor_bars": [['호박', 4], ['밤', 3], ['말차', 3], ['딸기', 3], ['초코', 2]],
        "pack_bars": [['편의점 단독', 4], ['크리스피 샌드', 3], ['케이크바 신규라인', 2], ['미니컵', 2], ['콜라보 캠페인', 2]],
        "content_bars": [['하겐다즈 호박타르트 모그나비 랭킹', 12], ['하겐다즈 크레이지버터 역주행', 8], ['데일리야마자키x배스킨라빈스 콜라보 보도', 5], ['세븐일레븐 코메다 콜라보 보도', 4], ['모리나가 MOW 신상 보도', 3]],
        "refs_intro": '이번 주 일본 섹션은 하겐다즈·세븐일레븐·글리코 등의 11월 신상 정리 기사와 모그나비 랭킹 데이터를 중심으로 조사했다.',
        "refs": [{'num': 1, 'title': '모그나비 주간 아이스크림 랭킹', 'note': '하겐다즈 호박타르트 1위 유지, 크레이지버터 급상승 소식', 'kind': '기사', 'thumb_url': None}, {'num': 2, 'title': 'entabe 11월 신상 아이스 정리', 'note': '세븐일레븐·글리코·롯데·모리나가 11월 신상 정리', 'kind': '기사', 'thumb_url': None}, {'num': 3, 'title': 'entabe 가을·겨울 신상 과자·아이스 정리', 'note': '하겐다즈 케이크바·아카기 신상 정리', 'kind': '기사', 'thumb_url': None}, {'num': 4, 'title': 'convenicheck 데일리야마자키 배스킨라빈스 신상', 'note': '편의점 단독 콜라보 신상 소식', 'kind': '기사', 'thumb_url': None}, {'num': 5, 'title': '모그나비 아이스 신상 전체', 'note': '이무라야 호지차 와라비 아이스 인기 지속 소식', 'kind': '기사', 'thumb_url': None}],
    },
]
OVERVIEW = {
    "highlights": [('#6B4226', '한국: GS25 초코바 신상 화제 속 배스킨라빈스 가격 5.9% 인상'), ('#B8912A', '미국: 패트보이·콜드스톤 홀리데이 시즌 스틱·샌드위치 신상 출시'), ('#A66A1C', '일본: 하겐다즈 호박 타르트, 모그나비 주간 랭킹 1위 유지')],
    "table_rows": [('한국', '초코', '2', '2', '초코', '#EFDDD0'), ('미국', '바닐라', '3', '0', '바닐라', '#FFFBEF'), ('일본', '호박', '8', '1', '호박', '#F3E3D8')],
    "analysis": "이번 주 세 시장을 종합하면, 한국은 초콜릿 맛과 가격 이슈가 동시에 부각되며 GS25의 초코바 신상이 SNS 화제를 이끈 반면 배스킨라빈스는 가격 인상으로 반대 흐름을 보였다. 미국은 홀리데이 시즌을 겨냥한 스틱·샌드위치 포맷 신상이 중심이었고, 아직 대형 체인의 공식 11월 신메뉴 발표가 뚜렷하지 않아 다음 주 추가 발표 가능성이 남아 있다. 일본은 10월 출시된 하겐다즈 호박 타르트가 한 달 가까이 모그나비 주간 랭킹 1위를 지키며 '화제성의 지속성'이 눈에 띄었고, 밤·말차 등 가을 정서 맛과 편의점 단독 콜라보가 신제품 수를 끌어올렸다. 세 시장 모두 편의점·대형 체인이 신상 발표의 중심이라는 공통점을 보였으며, 글로벌 브랜드(배스킨라빈스·세븐일레븐)는 한국과 일본에서 각기 다른 방식(가격 인상 vs 콜라보 신상)으로 이번 주 화제를 만들었다. 다음 주에도 가을 정서의 맛과 가격·콜라보 이슈가 동시에 이어질 가능성이 높다.",
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
