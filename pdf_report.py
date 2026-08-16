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

REPORT_DATE = '2026.08.16'
REPORT_RANGE = '2026.08.09 - 08.16'
OUT_PDF = 'docs/reports/2026-08-16-ice-cream-trends.pdf'

COUNTRIES = [{'key': 'kr', 'name': '한국', 'flavor': '레몬', 'soft': '#FFFDE0', 'mid': '#F5E36A', 'deep': '#C9B71B', 'headline': '레몬향 신맛 챌린지와 K팝 콜라보가 편의점 아이스크림을 흔들다', 'summary_paragraphs': ["GS25가 TXT 연준과 손잡고 낸 사워레몬요거트 컵·바가 초도 물량 약 4만개를 완판시키며 K팝 콜라보 마케팅에 다시 불을 지폈습니다. 아이브·키키(KiiiKiii)에 이은 세 번째 아이돌 협업으로, 요아정·로로멜로와 함께 만든 컵(4,500원)·바(2,500원) 2종 모두 SNS에서 빠르게 품절 인증이 이어졌습니다. 세븐일레븐의 3단계 신맛 챌린지 '시다바'는 출시 몇 주가 지나도 Threads·X·틱톡에서 계속 회자되며 장수 바이럴의 사례를 보여주고 있습니다.", "롯데웰푸드는 손시림 방지 패키지로 리뉴얼한 '설레임'에 이어 벨지안 초콜릿·멜론소다 맛 '쿨리쉬' 신제품을 선보였고, 해태는 알룰로스로 원조 맛을 살린 제로슈거 아이스바 4종을 출시하며 저당 트렌드에 가세했습니다. 기록적인 폭염 속에 GS25 아이스크림 매출은 전년 대비 23.6% 늘었고, 얼음컵 등 인접 냉동·냉장 디저트 매출도 최대 39% 뛰었습니다. 배스킨라빈스는 신제품 대신 고객 참여형 '그래이맛 콘테스트' 상위 3종을 공개하며 팬 투표 열기를 이어가고 있습니다."], 'flavor_bars': [['레몬/신맛', 6], ['딸기/산딸기', 5], ['망고', 3], ['복숭아/포도', 3], ['요거트', 2]], 'pack_bars': [['바', 8], ['콜라보 굿즈', 5], ['컵', 3], ['빙수', 3], ['소르베', 3]], 'content_bars': [['GS25 연준 콜라보 완판 소식 확산', 5], ['시다바 신맛챌린지 반복 공유', 4], ["TXT 'Ice Cream' 안무 숏폼", 3]], 'refs_intro': '이번 주 한국 시장에서 참고한 뉴스·SNS·공식 채널 자료입니다. 인스타그램·틱톡 전체를 크롤링한 것이 아니라 웹검색으로 확인 가능한 범위의 게시물만 반영했습니다.', 'refs': [{'num': '1', 'title': 'GS25 사워레몬요거트 초도 완판', 'note': 'TXT 연준과 협업한 컵·바 2종, 초도 물량 약 4만개 매진 — 이투데이', 'kind': '뉴스', 'thumb_url': None}, {'num': '2', 'title': '롯데웰푸드 젤리 채운 쿨리쉬 확대', 'note': '벨지안 초콜릿·멜론소다 맛 쿨리쉬 신제품 출시 — 이트뉴스', 'kind': '뉴스', 'thumb_url': None}, {'num': '3', 'title': '해태 제로슈거 아이스바 4종', 'note': '알룰로스로 원조 맛 살린 0g당·0kcal 신제품 — 더페어뉴스', 'kind': '뉴스', 'thumb_url': None}, {'num': '4', 'title': '세븐일레븐 시다바 신맛 챌린지', 'note': '신맛 3단계 챌린지 영상이 여러 계정에서 반복 공유 — 세븐일레븐 공식 X', 'kind': 'SNS', 'thumb_url': None}, {'num': '5', 'title': 'GS25 아이스크림 매출 23.6% 증가', 'note': 'K팝 협업 마케팅 효과로 7월~8월 초 매출 급증 — 뉴스웨이', 'kind': '뉴스', 'thumb_url': None}, {'num': '6', 'title': '폭염에 편의점 얼음컵 매출 39% 급증', 'note': '아이스크림 인접 카테고리까지 폭염 수혜 — 뉴스1', 'kind': '뉴스', 'thumb_url': None}]}, {'key': 'us', 'name': '미국', 'flavor': '초코', 'soft': '#EFDDD0', 'mid': '#C89173', 'deep': '#6B4226', 'headline': '초콜릿·피스타치오 강세 속 워터멜론 아이스크림이 SNS를 강타하다', 'summary_paragraphs': ['노처른 수박 아이스크림 레시피가 한 달 새 SNS 언급량이 13배 넘게 뛰며 올여름 최대 바이럴 트렌드로 떠올랐습니다. 수박을 반으로 갈라 속을 파내고 생크림을 부어 얼리기만 하면 완성되는 간단한 방식이 브랜드 신제품보다 더 큰 화제성을 만들어내고 있습니다. 두바이 초콜릿·피스타치오 조합은 콜드스톤·배스킨라빈스·린트 등 여러 브랜드가 연이어 출시하며 여전히 카테고리 전체에서 가장 꾸준한 강세를 보이고 있습니다.', "7-Eleven은 드럼스틱과 손잡고 블루라즈베리 바닐라 맛 '슬러피 콘'을 전국에 선보였고, 하겐다즈는 다크체리 트러플·커피 아몬드 토피 등 프리미엄 미니바 6종으로 소용량 시장을 공략했습니다. 콜드스톤은 '캐러멜 트러플' 신메뉴를, 페리스 아이스크림은 프리클리페어 라임 등 매운맛 신제품과 비건 귀리크림 베이스를 함께 출시했습니다. 매사추세츠의 한 아이스크림 트럭 기사가 돈이 없는 아이에게 아이스크림을 무료로 건넨 영상은 860만 회 넘게 재생되며 기부 캠페인으로 이어졌습니다."], 'flavor_bars': [['초콜릿', 8], ['피스타치오', 6], ['카라멜', 5], ['땅콩버터', 4], ['쿠키도우', 4]], 'pack_bars': [['파인트/카톤', 6], ['미니바', 5], ['샌드위치', 4], ['콘', 3], ['블리자드/선데', 5]], 'content_bars': [['워터멜론 아이스크림 챌린지', 6], ['아이스크림트럭 무료나눔 영상', 5]], 'refs_intro': '이번 주 미국 시장에서 참고한 뉴스·공식 발표 자료입니다. 인스타그램·틱톡 전체를 크롤링한 것이 아니라 웹검색으로 확인 가능한 범위의 게시물만 반영했습니다.', 'refs': [{'num': '1', 'title': '7-Eleven x Drumstick 슬러피 콘', 'note': '블루라즈베리 바닐라 맛 콘, 여름 프로즌 스낵으로 전국 출시 — KTLA', 'kind': '뉴스', 'thumb_url': None}, {'num': '2', 'title': '워터멜론 아이스크림 챌린지 바이럴', 'note': '노처른 수박 레시피, 한 달 새 언급량 13배 급증 — Fast Company', 'kind': '영상', 'thumb_url': 'https://img.youtube.com/vi/Qgu5XWtnTpI/hqdefault.jpg'}, {'num': '3', 'title': '하겐다즈 프리미엄 미니바 6종', 'note': '다크체리 트러플 등 카톤·미니바 신제품 확대 — Parade', 'kind': '뉴스', 'thumb_url': None}, {'num': '4', 'title': '콜드스톤 캐러멜 트러플 신메뉴', 'note': '캐러멜·초콜릿 트러플 결합 신메뉴 출시 — Chewboom', 'kind': '뉴스', 'thumb_url': None}, {'num': '5', 'title': '페리스 아이스크림 신맛 라인업', 'note': "프리클리페어 라임 등 신맛과 비건 귀리크림 베이스 출시 — Perry's Ice Cream", 'kind': '뉴스', 'thumb_url': None}, {'num': '6', 'title': '아이스크림트럭 무료 나눔 영상 860만뷰', 'note': '매사추세츠 트럭 기사의 무료 나눔 영상이 기부 캠페인으로 확산 — Today.com', 'kind': 'SNS', 'thumb_url': None}, {'num': '7', 'title': '틸라묵 뉴욕 팝업 스탠드', 'note': '인플루언서와 함께한 무료 시식 팝업 및 경품 이벤트 — Trend Hunter', 'kind': '뉴스', 'thumb_url': None}]}, {'key': 'jp', 'name': '일본', 'flavor': '초코민트', 'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C', 'headline': '초코민트 삼파전 속 배·샤인머스캣 프리미엄 과일 맛이 인기', 'summary_paragraphs': ["모리나가·서티원·맥도날드가 한 주 사이 나란히 초코민트 신제품을 내놓으며 여름 대표 맛 경쟁이 뜨거워졌습니다. 맥도날드는 걸그룹 HANA 멤버를 내세운 새 TV 광고와 함께 '쿠키&초코민트 프라페'를 2년 만에 재출시하며 8월 19일부터 판매합니다. 서티원은 포켓몬 30주년을 기념한 '31포케 여름' 캠페인으로 피카츄 테마 한정판 소다맛 신메뉴와 몬스터볼 컵을 앞세워 팬덤 마케팅에 나섰습니다.", "세븐일레븐은 스트로우로 망고 와라비모찌와 요거트 밀크를 섞어 먹는 새로운 형태의 컵 디저트를 8월 11일부터 순차 발매했고, 하겐다즈는 땅콩버터 소스를 채운 크리스피 샌드 신제품을 8월 18일부터 한정 판매합니다. 롯데 '爽'는 과즙·과육 7%를 담은 샤인머스캣 셔벗을 '럭셔리 시리즈' 네 번째 제품으로 8월 17일 전국 발매합니다. 패밀리마트의 배 맛 아이스 '사쿠레 나시'는 여름 아이스 랭킹 방송에서 1위에 오르며 SNS에서 품절 인증 게시물이 잇따르고 있습니다."], 'flavor_bars': [['초코민트', 4], ['나시(배)', 3], ['샤인머스캣', 3], ['소금카라멜/피스타치오', 3], ['망고', 2]], 'pack_bars': [['카톤/카톤 셔벗', 4], ['믹스&매치 컵 디저트', 3], ['크리스피 샌드', 2], ['프라페', 2], ['소다맛 신메뉴', 2]], 'content_bars': [['사쿠레 나시 TV 랭킹 1위 화제', 4], ['파피코 말차 나마초코라떼 재등장', 3]], 'refs_intro': '이번 주 일본 시장에서 참고한 뉴스·공식 채널 자료입니다. 인스타그램·틱톡 전체를 크롤링한 것이 아니라 웹검색으로 확인 가능한 범위의 게시물만 반영했습니다.', 'refs': [{'num': '1', 'title': '세븐일레븐 망고&요거트 믹스 디저트', 'note': '스트로우로 섞어 먹는 새 형태 컵 디저트, 8월 11일 발매 — tokubai', 'kind': '뉴스', 'thumb_url': None}, {'num': '2', 'title': '하겐다즈 땅콩버터 크리스피 샌드', 'note': '버터캐러멜 아이스에 땅콩버터 소스, 8월 18일 한정 판매 — ハーゲンダッツ公式', 'kind': '뉴스', 'thumb_url': None}, {'num': '3', 'title': '서티원 31포케 여름 캠페인', 'note': '포켓몬 30주년 기념 피카츄 테마 캠페인, 8월 한 달 진행 — br31.jp', 'kind': '뉴스', 'thumb_url': None}, {'num': '4', 'title': '패밀리마트 사쿠레 나시 TV 랭킹 1위', 'note': '배 맛 아이스가 여름 랭킹 방송 1위 후 SNS서 품절 잇따름 — Yahoo!リアルタイム検索', 'kind': 'SNS', 'thumb_url': None}, {'num': '5', 'title': '맥도날드 초코민트 프라페 재출시', 'note': '2년 만의 재출시, HANA 멤버 출연 새 TVCM — マクドナルド公式', 'kind': '뉴스', 'thumb_url': None}, {'num': '6', 'title': '파피코 말차 나마초코라떼 재등장', 'note': '재출시 소식에 X에서 리포스트 인증 확산 — X(@PAPICO_JPN)', 'kind': 'SNS', 'thumb_url': None}]}]

OVERVIEW = {'highlights': [('#C9B71B', '한국: GS25 사워레몬요거트, K팝 콜라보 초도 4만개 완판'), ('#6B4226', '미국: 워터멜론 아이스크림 챌린지, 한 달새 SNS 언급 13배 급증'), ('#A66A1C', '일본: 초코민트 삼파전, 모리나가·서티원·맥도날드 동시 출시')], 'table_rows': [('한국', '레몬', '3건', '1건', '레몬/신맛 · 딸기', '#FFFDE0'), ('미국', '초코', '4건', '2건', '초콜릿 · 피스타치오', '#EFDDD0'), ('일본', '초코민트', '3건', '1건', '초코민트 · 나시(배)', '#F3E3D8')], 'analysis': "이번 주는 세 시장 모두 '한정판 콜라보'와 '자생적 바이럴 챌린지'가 소비자 반응을 이끄는 두 축으로 자리 잡았습니다. 한국은 GS25가 TXT 연준과 협업한 사워레몬요거트로 K팝 팬덤 마케팅의 힘을 다시 입증했고, 세븐일레븐의 신맛 챌린지는 출시 몇 주가 지나도 SNS에서 꾸준히 회자되며 장수 바이럴의 사례를 보여줬습니다. 미국은 노처른 수박 아이스크림이라는 자생적 레시피 트렌드가 브랜드 신제품보다 더 큰 화제성을 만들어냈고, 하겐다즈·콜드스톤 등은 프리미엄 소용량 포맷으로 이에 대응하고 있습니다. 일본은 초코민트라는 스테디셀러 맛을 두고 편의점·패스트푸드 브랜드가 동시다발적으로 신제품을 내놓으며 여름 정례 경쟁 구도를 재확인시켰습니다. 세 시장 공통적으로 브랜드 단독 신제품보다 협업·챌린지·팬덤 요소가 결합된 콘텐츠가 더 큰 반응을 얻고 있다는 점이 눈에 띕니다."}

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
