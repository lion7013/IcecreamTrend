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

REPORT_DATE = "2026.09.13"
REPORT_RANGE = "2026.09.07 - 09.13"
OUT_PDF = "docs/reports/2026-09-13-ice-cream-trends.pdf"
COUNTRIES = [
    {
        'key': 'kr', 'name': '한국', 'flavor': '고구마',
        'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C',
        'headline': '요아정 가을 신메뉴와 세븐일레븐 이색 바가 이끈 한 주',
        'summary_paragraphs': [
            "요아정이 제철 무화과와 얼린 고구마맛탕 토핑을 결합한 가을 한정 메뉴를 추석 시즌에 맞춰 선보이며 SNS에서 꾸준한 화제를 모았습니다. 롯데웰푸드는 경북 군위산 사과를 테마로 한 '위즐 애플잼크림 모나카'와 '조이 그릭요거트 군위사과 애플' 등 신제품 2종을 출시하고 서울역 KTX 팝업으로 이를 알렸습니다. 두 브랜드 모두 제철 국산 농산물을 전면에 내세운 것이 특징입니다.",
            "세븐일레븐은 신맛 강도를 3단계로 나눈 '시다바'와 망고스틴 과육과 껍질 모양을 살린 '망고스틴바'를 잇달아 선보이며 편의점 신상 경쟁에 활기를 더했습니다. 배스킨라빈스는 매장 평균 가격을 약 8% 인상한 가운데도 9월 한 달간 500원 추가로 주니어를 더블주니어로 업그레이드해주는 프로모션을 진행하며 소비자 접점을 늘리고 있습니다. 편의점발 이색 신상 비교 콘텐츠도 SNS와 유튜브 쇼츠에서 꾸준히 공유되고 있습니다.",
        ],
        'flavor_bars': [['고구마', 22], ['사과', 15], ['레몬·신맛', 13], ['무화과', 12], ['초코', 10]],
        'pack_bars': [['컵 타입', 16], ['바 타입', 15], ['포토카드·스티커 동봉', 14], ['콘', 11], ['모나카·샌드 타입', 9]],
        'content_bars': [['세븐일레븐 시다바 SNS', 9], ['세븐일레븐 망고스틴바', 7], ['요아정 가을 신메뉴', 6], ['편의점 신상 쇼츠', 5], ['배스킨라빈스 가격 인상', 4]],
        'refs_intro': '이번 리포트는 국내 언론사 기사와 X·Threads 등 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체를 실시간 크롤링한 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': "요아정, 무화과·아이스고구마맛탕 가을 신메뉴 출시", 'note': '헤럴드경제, 추석 시즌 가을 신메뉴 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': "롯데웰푸드, '군위 사과' 테마 빙과 신제품 2종 출시", 'note': '넥스트데일리, 군위 사과 신제품 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': "세븐일레븐, 신맛 3단계 '시다바' 공식 SNS 공개", 'note': '세븐일레븐 공식 X, 신맛 단계별 아이스바 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 4, 'title': '배스킨라빈스, 매장 평균 가격 약 8% 인상', 'note': 'SBS Biz, 매장 가격 인상 보도.', 'kind': '뉴스', 'thumb_url': None},
            {'num': 5, 'title': "유튜브 쇼츠 '이색 편의점 신상 아이스크림 3가지' 화제", 'note': '유튜브 쇼츠, 편의점 신상 비교 콘텐츠.', 'kind': '바이럴', 'thumb_url': None},
        ],
    },
    {
        'key': 'us', 'name': '미국', 'flavor': '커피',
        'soft': '#EFE3D8', 'mid': '#B08968', 'deep': '#5C3A21',
        'headline': '블루벨 화이트초콜릿모카가 이끈 커피맛 아이스크림 열풍',
        'summary_paragraphs': [
            "블루벨이 커피 아이스크림에 화이트초콜릿 조각과 바닐라 휘핑크림 스월을 더한 '화이트초콜릿모카'를 출시해 전국 지역 뉴스에서 같은 날 일제히 보도되며 이번 주 가장 화제가 된 신제품으로 떠올랐습니다. 배스킨라빈스는 비스코프 쿠키 조각과 캐러멜 스월을 넣은 커스터드 아이스크림을 중심으로 셰이크·선데·케이크까지 확장한 가을 한정 '비스코프 크렘브륄레' 컬렉션을 선보였습니다.",
            "데어리퀸은 브라운슈거 쿠키도우 블리자드를 출시하는 동시에 실제 대학 마스코트가 등장하는 다큐멘터리풍 광고 캠페인 '딥 치킨, 낫 마스코트'를 공개하며 가을 시즌 마케팅에 힘을 실었습니다. 제니스는 헤이즐넛 스트라치아텔라 등 가을 신맛 4종을 로스앤젤레스 매장에서 선보였고, 콜드스톤은 호박 대신 그레이엄 크래커를 활용한 '크럼 앤 겟 잇'을 11월 17일까지 판매하며 가을 신메뉴 경쟁에 합류했습니다. 탈렌티 역시 초콜릿 헤이즐넛 크런치 젤라토와 유제품 무첨가 패션프루트 소르베토를 새로 선보이며 라인업을 넓혔습니다.",
        ],
        'flavor_bars': [['펌킨·펌킨스파이스', 27], ['브라운슈거 쿠키도우', 21], ['커피·모카', 19], ['피스타치오·두바이초콜릿', 15], ['비스코프·캐러멜', 13]],
        'pack_bars': [['파인트', 24], ['싱글서브·미니컵', 18], ['바·미니바', 16], ['멀티레이어 자', 12], ['종이·친환경 패키징', 9]],
        'content_bars': [['블루벨 전국 보도', 14], ['데어리퀸 리뷰 화제', 8], ['배스킨라빈스 비스코프', 7], ['제니스 가을 컬렉션', 6], ['콜드스톤 신메뉴', 5]],
        'refs_intro': '이번 주 미국 시장 리서치는 현지 언론과 웹검색으로 확인 가능한 정보를 기반으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': 'Blue Bell Releases New White Chocolate Mocha Flavor', 'note': 'FOX 4 Dallas-Fort Worth, 전국 지역 뉴스 동시 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': "Baskin Robbins Brings a Taste of Travel to Fall With Biscoff Collection", 'note': 'Inspire Brands Newsroom, 가을 한정 컬렉션 출시.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': "Dairy Queen Brown Sugar Cookie Dough Blizzard Review", 'note': 'The Impulsive Buy, 신메뉴 리뷰 화제.', 'kind': '신제품', 'thumb_url': None},
            {'num': 4, "title": "Jeni's Fall Ice Cream Collection Arrives in Los Angeles", 'note': 'Yo! Venice, 가을 신맛 컬렉션 출시 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 5, 'title': 'Dairy Queen Capitalizes on Social Documentary Trend to Launch LTOs', 'note': 'MediaPost, 마스코트 광고 캠페인 소개.', 'kind': '광고', 'thumb_url': None},
        ],
    },
    {
        'key': 'jp', 'name': '일본', 'flavor': '호지차',
        'soft': '#F1E4D3', 'mid': '#C9A579', 'deep': '#8B5E34',
        'headline': '롯데·모리나가 가격 인상 속 호지차 신제품 3종 동시 출격',
        'summary_paragraphs': [
            "모리나가 '파르므'가 화이트초콜릿으로 감싼 호지차라테 맛을 5년 만에 재출시했고, 로손은 진하게 볶은 호지차 아이스크림에 밀크맛 와플콘을 결합한 '호지차 와플콘'을 내놓았습니다. 이무라야 역시 우지 호지차와 시리즈 최초로 흑설탕 와라비모찌를 층층이 쌓은 모찌 아이스를 편의점 우선 출시하며, 이번 주 일본 편의점·유업계는 호지차 신제품 삼중주로 채워졌습니다.",
            "같은 시기 롯데는 쿨리시 등 35개 아이스크림 품목의 가격을 9월 1일 출하분부터 5.1~16.0% 인상했다고 발표하며 인건비·물류비 상승을 배경으로 꼽았습니다. 이런 가운데 세븐프리미엄의 티라미수맛 미세빙수 디저트 '티라미수 고리'는 편의점 아이스크림 주간 랭킹 1위 자리를 지키며 '고리 스위츠' 붐을 이끌고 있다는 평가를 받았고, 배스킨라빈스 재팬은 후지야 밀키·페코짱과 두 번째로 손잡은 '밀키 원더랜드' 컬래버레이션으로 쇼트케이크맛 신규 플레이버와 한정 더블컵을 선보였습니다.",
        ],
        'flavor_bars': [['호지차', 27], ['티라미수·커피', 22], ['캐러멜', 18], ['피스타치오', 15], ['밀크·밀키', 14]],
        'pack_bars': [['미니컵', 24], ['바·스틱', 20], ['고리(빙수) 컵', 18], ['와플콘', 16], ['어소트박스', 12]],
        'content_bars': [['세븐일레븐 티라미수고리 1위', 22], ['모리나가 호지차라테 재출시', 14], ['롯데 가격 인상 뉴스', 12], ['로손 호지차 와플콘', 9], ['배스킨라빈스재팬 밀키 콜라보', 8]],
        'refs_intro': '이 섹션은 일본 언론·업계 매체 기사와 웹검색으로 확인 가능한 정보를 바탕으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': "모리나가 '파르므', 호지차라테 맛 5년 만에 재출시", 'note': '모리나가유업 공식 발표, 재출시 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': "로손, '호지차 와플콘' 신메뉴 출시", 'note': '진격의 구르메, 로손 신상 소개.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': "세븐일레븐 '티라미수 고리', 편의점 아이스 랭킹 1위 지켜", 'note': '세븐프리미엄, 주간 랭킹 1위 소식.', 'kind': '바이럴', 'thumb_url': None},
            {'num': 4, 'title': "롯데, 아이스크림 35개 품목 가격 5.1~16% 인상", 'note': 'Impress Watch, 9월 가격 인상 보도.', 'kind': '뉴스', 'thumb_url': None},
            {'num': 5, 'title': "배스킨라빈스 재팬×후지야, 두 번째 '밀키' 협업 공개", 'note': '패션프레스, 밀키 원더랜드 콜라보 소식.', 'kind': '신제품', 'thumb_url': None},
        ],
    },
]
OVERVIEW = {
    'highlights': [
        ('#A66A1C', '한국, 요아정 가을 신메뉴와 세븐일레븐 이색 바가 편의점 경쟁 주도'),
        ('#5C3A21', '미국, 블루벨 화이트초콜릿모카가 전국 뉴스에 오르며 커피맛 열풍 견인'),
        ('#8B5E34', '일본, 롯데·모리나가 가격 인상 속 호지차 신제품 3종 동시 출시'),
    ],
    'table_rows': [
        ('한국', '고구마', '4', '1', '고구마·사과', '#F3E3D8'),
        ('미국', '커피', '6', '0', '브라운슈거·커피', '#EFE3D8'),
        ('일본', '호지차', '5', '1', '호지차·티라미수', '#F1E4D3'),
    ],
    'analysis': '이번 주(9/7~9/13) 세 시장은 저마다 다른 방식으로 가을 시즌 전환을 준비했습니다. 한국은 요아정의 무화과·고구마맛탕 신메뉴와 롯데웰푸드의 군위 사과 라인이 국산 제철 농산물을 앞세운 반면, 세븐일레븐은 신맛 단계별 시다바와 과일 모양 아이스바로 편의점 신상 경쟁을 이어갔습니다. 미국은 블루벨의 화이트초콜릿모카가 전국 지역 뉴스를 통해 가장 넓게 확산된 신제품으로 떠올랐고, 브라운슈거·펌킨스파이스 등 가을 정통 풍미가 신맛 트렌드의 중심을 차지했습니다. 일본은 모리나가·로손·이무라야가 한 주 사이 나란히 호지차 신제품을 내놓으며 가장 뚜렷한 단일 맛 쏠림을 보였고, 동시에 롯데가 35개 품목 가격을 최대 16% 인상하며 원가 압박이 표면화됐습니다. 세 시장 공통적으로 편의점·프랜차이즈의 신상 주기는 빨라지는 반면, 일본에서는 가격 인상이 먼저 현실화되고 있다는 점이 대조적입니다.',
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
