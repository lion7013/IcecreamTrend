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

REPORT_DATE = '2026.08.10'
REPORT_RANGE = '2026.08.03 - 08.10'
OUT_PDF = 'docs/reports/2026-08-10-ice-cream-trends.pdf'

COUNTRIES = [{'key': 'kr', 'name': '한국', 'flavor': '딸기', 'soft': '#FCEAF0', 'mid': '#F6A9BE', 'deep': '#C85476', 'headline': '폭염 속 딸기·콜라보 아이스크림이 편의점을 휩쓸다', 'summary_paragraphs': ["낮 최고기온이 연일 기록을 경신하는 폭염이 이어지면서 아이스크림 검색량이 전주 대비 3배 급증했습니다. 배스킨라빈스는 산딸기에 연유를 더한 맛을 8월 이달의 맛으로 내세우고 여름 한정 와그작 빙수 3종을 함께 선보였으며, 세븐일레븐은 신맛을 3단계로 나눠 도전하는 '시다바'와 리얼 과육 망고스틴바로 SNS 화제를 모았습니다. GS25는 걸그룹 키키(KiiiKiii)와 협업한 딸기·망고 젤라또바를 선보이며 출시 두 달째에도 꾸준한 판매를 이어가고 있습니다.", "롯데웰푸드는 죠스바·스크류바에 젤리를 넣은 신제품과 필리핀산 우베를 활용한 이색 라인으로 잘파세대를 공략했고, 웹툰작가 기안84를 '설레임' 모델로 발탁해 마케팅을 강화했습니다. 빙그레는 더위사냥 저당·디카페인 버전 등 헬시플레저 라인을 확대하며 당 함량을 낮춘 트렌드에 합류했습니다. 한편 투모로우바이투게더 연준의 신곡 'Ice Cream'이 음원 차트 1위에 오르며 실제 제품과 무관하게 검색 노출을 함께 끌어올린 점도 눈에 띕니다."], 'flavor_bars': [['딸기', 12], ['망고', 8], ['신맛/사워', 5], ['커피', 4], ['우베', 3]], 'pack_bars': [['콜라보 패키지', 10], ['리미티드 에디션', 7], ['미니바/미니컵', 6], ['저당·헬시 라벨', 5], ['대용량 파인트', 3]], 'content_bars': [['신상아이스크림 총정리(Threads)', 4], ["TXT 연준 'Ice Cream' 차트1위", 3], ['신맛 리뷰(Threads)', 2], ['철판아이스크림 쇼츠', 2]], 'refs_intro': '이번 주 한국 시장에서 참고한 뉴스·SNS·공식 채널 자료입니다. 인스타그램·틱톡 전체를 크롤링한 것이 아니라 웹검색으로 확인 가능한 범위의 게시물만 반영했습니다.', 'refs': [{'num': '1', 'title': '배스킨라빈스 8월 이달의 맛', 'note': '산딸기 연유를 8월 이달의 맛으로 공개, 박지훈을 모델로 통합 마케팅 전개 — 한국경제', 'kind': '뉴스', 'thumb_url': None}, {'num': '2', 'title': 'GS25 키키(KiiiKiii) 젤라또바', 'note': 'K팝 걸그룹과 협업한 딸기·망고 젤라또바, 2,000원대 가격에 지속 판매 중 — 다음뉴스', 'kind': '뉴스', 'thumb_url': None}, {'num': '3', 'title': '세븐일레븐 신맛질주 시다바', 'note': '신맛 3단계 도전형 아이스바, 2+1 프로모션으로 판매 — 세븐일레븐 공식 X', 'kind': 'SNS', 'thumb_url': None}, {'num': '4', 'title': '신상 아이스크림 17개 총정리', 'note': '올여름 신상 아이스크림을 정리한 인플루언서 콘텐츠 — Threads', 'kind': 'SNS', 'thumb_url': None}, {'num': '5', 'title': '철판 즉석 롤아이스크림 쇼츠', 'note': '철판 위에서 즉석 롤아이스크림을 만드는 콘텐츠가 화제 — YouTube Shorts', 'kind': '영상', 'thumb_url': 'https://img.youtube.com/vi/g-gPtU2w3yo/hqdefault.jpg'}, {'num': '6', 'title': '폭염에 아이스크림 검색량 3배 급증', 'note': '신세계라이브쇼핑, 검색량 급증 데이터 근거로 빙과류 최대 60% 할인전 — 이코노미사이언스', 'kind': '뉴스', 'thumb_url': None}]}, {'key': 'us', 'name': '미국', 'flavor': '딸기', 'soft': '#FCEAF0', 'mid': '#F6A9BE', 'deep': '#C85476', 'headline': '딸기·브루키 조합이 미국 여름 아이스크림을 점령하다', 'summary_paragraphs': ["검색 트렌드 분석 결과 딸기가 올여름 미국인이 가장 좋아하는 아이스크림 맛으로 나타난 가운데, 이번 주 신제품 다수가 베리 계열로 쏠렸습니다. 배스킨라빈스는 브라운슈가·브라우니 아이스크림에 오레오와 쿠키도우를 섞은 '브루키 배터'를 8월 이달의 맛으로 선정했고, 데어리퀸은 치즈케이크 조각과 캐러멜 애플 토핑을 소프트서브에 섞은 블리자드를 출시하며 앱 회원 대상 2개째 99센트 프로모션을 함께 진행했습니다.", "벤앤제리스는 시애틀 파이어62에서 무료 아이스크림바 배포 투어를 열어 신규 PB 프레첼·캐러멜 블론디 바를 선보였고, 험프리 슬로컴은 공포영화 '아이스크림 맨' 개봉에 맞춰 딸기잼을 섞은 버블검맛 한정판을 전국 배송으로 판매했습니다. 코스트코의 망고·복숭아 모양 3D 과일 아이스크림은 SNS에서 재확산되며 매대에서 빠르게 팔려나갔고, 피스타치오-쿠나파 조합의 '두바이 초콜릿' 풍미도 검색량이 전년 대비 약 450% 늘며 계속 확산되고 있습니다."], 'flavor_bars': [['딸기/베리', 9], ['브루키', 7], ['캐러멜', 6], ['치즈케이크', 5], ['망고/복숭아', 5]], 'pack_bars': [['한정판', 12], ['파인트', 7], ['노벨티 바', 6], ['하프갤런', 4], ['3D 과일 쉘', 4]], 'content_bars': [['코스트코 3D 과일 아이스크림', 5], ["영화 '아이스크림맨' 흥행 화제", 3]], 'refs_intro': '이번 주 미국 시장에서 참고한 뉴스·공식 발표 자료입니다. 인스타그램·틱톡 전체를 크롤링한 것이 아니라 웹검색으로 확인 가능한 범위의 게시물만 반영했습니다.', 'refs': [{'num': '1', 'title': 'Dairy Queen 캐러멜 애플 치즈케이크 블리자드', 'note': '8월 블리자드 오브 더 먼스, 앱 회원 2개째 99센트 프로모션 동시 진행 — Daily Voice', 'kind': '뉴스', 'thumb_url': None}, {'num': '2', 'title': "Baskin Robbins '브루키 배터'", 'note': '브라우니·쿠키도우를 섞은 8월 이달의 맛, 한 달 내내 판매 — The Impulsive Buy', 'kind': '뉴스', 'thumb_url': None}, {'num': '3', 'title': "Ben & Jerry's 시애틀 무료 배포 투어", 'note': '황금 막대 5개를 찾으면 1년치 아이스크림바를 받는 전국 투어 — PR Newswire', 'kind': '뉴스', 'thumb_url': None}, {'num': '4', 'title': '코스트코 3D 과일 모양 아이스크림', 'note': '망고·복숭아 모양 껍질을 깨먹는 노벨티 아이스크림이 SNS에서 재확산 — Parade', 'kind': 'SNS', 'thumb_url': None}, {'num': '5', 'title': '올여름 미국 1위 맛은 딸기', 'note': '검색 트렌드 분석 결과 딸기가 미국인이 가장 선호하는 맛으로 확인 — Mental Floss', 'kind': '뉴스', 'thumb_url': None}]}, {'key': 'jp', 'name': '일본', 'flavor': '초코민트', 'soft': '#EFDDD0', 'mid': '#C89173', 'deep': '#6B4226', 'headline': '초코민트 대전, 모리나가·세븐일레븐이 편의점을 물들이다', 'summary_paragraphs': ["모리나가가 초콜릿 껍질을 깨먹는 체험형 컵 아이스 '바리체 초코&민트'를 편의점에 선출시하고, 세븐일레븐도 같은 주에 초코민트 신제품을 내놓으면서 업계 데이터 기준 초코민트 카테고리 성장률이 눈에 띄게 뛰었습니다. 세븐일레븐은 이 외에도 마스카포네 풍미의 '티라미수 빙수'를 재출시하고 이무라야의 대표 팥바를 말차 버전으로 확장하는 등 라인업을 넓혔습니다.", "하겐다즈는 8월 10일 '하겐다즈 데이'에 맞춰 발표한 설문조사에서 피스타치오·솔티캐러멜을 올여름 가장 먹고 싶은 신제품 맛 1위로 선정했습니다. 서티원은 포켓몬과 협업한 수박 모양 '스이카 서머' 셔벗과 피카츄 콜라보 상품으로 팬들의 뜨거운 반응을 얻었고, 의류 브랜드 '47과 손잡고 클래식 맛에서 영감을 받은 야구모자를 8월 13일부터 전국 판매합니다. 홋카이도 멜론 와플콘 등 7월부터 이어진 멜론 인기도 세븐일레븐·훼미리마트에서 여전히 견조합니다."], 'flavor_bars': [['초코민트', 9], ['멜론', 6], ['말차', 5], ['피스타치오/솔티캐러멜', 4], ['수박', 3]], 'pack_bars': [['편의점 선출시', 7], ['수량한정·지역한정', 6], ['컵아이스', 6], ['콜라보 패키지', 4], ['바/스틱', 4]], 'content_bars': [['가마이타치 최신아이스 실식', 3], ['넷유저 극찬 아이스 8선', 3], ['서티원×피카츄 반응', 2]], 'refs_intro': '이번 주 일본 시장에서 참고한 뉴스·공식 채널·영상 자료입니다. 인스타그램·틱톡 전체를 크롤링한 것이 아니라 웹검색으로 확인 가능한 범위의 게시물만 반영했습니다.', 'refs': [{'num': '1', 'title': "모리나가 '바리체 초코&민트'", 'note': '편의점 선출시 후 8월 17일 전국 발매, 초코민트 카테고리 성장 견인 — 모리나가유업', 'kind': '뉴스', 'thumb_url': None}, {'num': '2', 'title': "하겐다즈 '올여름 1위 맛'", 'note': '하겐다즈 데이(8/10)에 맞춰 피스타치오·솔티캐러멜을 1위로 발표 — RBB Today', 'kind': '뉴스', 'thumb_url': None}, {'num': '3', 'title': "서티원 '스이카 서머' 수박 셔벗", 'note': '수박·멜론 셔벗과 초콜릿 씨앗으로 진짜 수박처럼 연출 — livedoor NEWS', 'kind': '뉴스', 'thumb_url': None}, {'num': '4', 'title': '서티원×포켓몬 피카츄 콜라보', 'note': '피카츄 기술명을 딴 콜라보 상품에 팬들 호응 — 포켓몬 공식 사이트', 'kind': 'SNS', 'thumb_url': None}, {'num': '5', 'title': '가마이타치 최신 편의점 아이스 실식', 'note': '개그 듀오가 2026년 최신 편의점 아이스를 먹어보는 인기 여름 포맷 — YouTube', 'kind': '영상', 'thumb_url': 'https://img.youtube.com/vi/nQ2wc6hqJY4/hqdefault.jpg'}]}]

OVERVIEW = {'highlights': [('#C85476', '한국: 검색량 3배 급증, 배스킨라빈스 산딸기 연유가 8월 이달의 맛 등극'), ('#C85476', "미국: 딸기가 올여름 1위 맛, '브루키 배터'·코스트코 3D 아이스 화제"), ('#6B4226', '일본: 모리나가·세븐일레븐 초코민트 동시 출시로 카테고리 급성장')], 'table_rows': [('한국', '딸기', '8건', '4건', '딸기 · 콜라보 패키지', '#FCEAF0'), ('미국', '딸기', '4건', '1건', '딸기/베리 · 한정판', '#FCEAF0'), ('일본', '초코민트', '5건', '2건', '초코민트 · 편의점 선출시', '#EFDDD0')], 'analysis': '이번 주는 폭염이 세 시장 모두의 소비 패턴에 직접적인 영향을 미친 한 주였습니다. 한국은 역대급 무더위 속에 아이스크림 검색량이 3배 급증하며 배스킨라빈스·GS25·세븐일레븐이 딸기·신맛 등 자극적인 맛으로 경쟁했고, 미국 역시 딸기가 올여름 1위 맛으로 조사되며 벤앤제리스·데어리퀸 등 대형 브랜드들이 여름 한정 프로모션을 쏟아냈습니다. 일본은 예년과 달리 초코민트가 멜론을 제치고 가장 뜨거운 카테고리로 떠올랐으며, 모리나가와 세븐일레븐이 같은 주에 경쟁 제품을 출시하면서 성장세를 견인했습니다. 세 시장 모두 아이돌·캐릭터·영화 등 엔터테인먼트 콜라보 마케팅이 활발했다는 공통점도 확인됐습니다. 다음 주에는 한국·미국의 폭염 프로모션 강도가 더 세질지, 일본의 초코민트 열풍이 얼마나 이어질지가 관전 포인트입니다.'}

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
