from pathlib import Path

W = 1080
BG = '#f5f9fb'
NAVY = '#15345b'
TEAL = '#1ea7a1'
LIGHT = '#e6f3f3'
CARD = '#ffffff'


def wrap_lines(text, limit=22):
    out=[]
    for para in text.split('\n'):
        if not para:
            out.append('')
            continue
        s=para
        while len(s)>limit:
            out.append(s[:limit])
            s=s[limit:]
        out.append(s)
    return out

def text_block(x,y,text,size=34,color=NAVY,lh=1.45,weight='700'):
    lines=wrap_lines(text,26 if size>=30 else 36)
    t=[]
    cy=y
    for ln in lines:
        t.append(f'<text x="{x}" y="{cy}" font-size="{size}" font-weight="{weight}" fill="{color}">{ln}</text>')
        cy += int(size*lh)
    return '\n'.join(t), cy

def page(title, sections, fname):
    h=3900
    y=0
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}">',
           f'<rect width="100%" height="100%" fill="{BG}"/>']
    parts += [f'<rect x="0" y="0" width="1080" height="250" fill="{CARD}"/>',
              f'<text x="70" y="105" font-size="40" font-weight="700" fill="{NAVY}">一般社団法人</text>',
              f'<text x="70" y="165" font-size="52" font-weight="800" fill="{NAVY}">日本みらい医療福祉共創協会</text>',
              f'<rect x="760" y="70" width="250" height="90" rx="45" fill="{TEAL}"/>',
              f'<text x="805" y="127" font-size="34" font-weight="700" fill="white">無料相談はこちら</text>']
    y=300
    parts.append(f'<text x="70" y="{y}" font-size="62" font-weight="800" fill="{NAVY}">{title}</text>')
    y += 70
    for sec in sections:
        y += 24
        parts.append(f'<rect x="50" y="{y}" width="980" height="{sec[0]}" rx="26" fill="{CARD}" stroke="{LIGHT}" stroke-width="3"/>')
        ty = y+60
        parts.append(f'<text x="85" y="{ty}" font-size="40" font-weight="800" fill="{TEAL}">{sec[1]}</text>')
        ty += 24
        content, _ = text_block(85, ty+38, sec[2], size=30, weight='500')
        parts.append(content)
        if sec[3]:
            by = y + sec[0]-105
            parts += [f'<rect x="85" y="{by}" width="560" height="72" rx="36" fill="{TEAL}"/>',
                      f'<text x="130" y="{by+47}" font-size="34" font-weight="700" fill="white">{sec[3]}</text>']
        y += sec[0]+20
    parts.append('</svg>')
    Path(fname).write_text('\n'.join(parts), encoding='utf-8')

pages=[
('トップ（HOME）',[
(840,'ファーストビュー','ひとりで悩む経営から、対話する経営へ。\nその悩み、私たちに話してください。\n医療・福祉・介護の経営に向き合うあなたの隣に、私たちはいます。\n\n中小企業診断士×福祉現場経験者のチームが、\n経営・人材・運営を一体で支援します。','まずは無料相談する →'),
(560,'課題と強み','経営の悩み／人材の悩み／運営の悩み\n・収益改善　・採用定着　・DX化推進\n\n強み\n1) 理論と現場をつなぐ\n2) 制度・現場・経営を同時に読む\n3) 答えを押しつけず伴走する','私たちの支援内容を見る →'),
(640,'支援概要と流れ','経営軸｜人材軸｜運営軸を一体支援\nSTEP1 事前アンケート（約5分）\nSTEP2 初回面談（無料・約60分）\nSTEP3 診断レポート（有償）\nSTEP4 継続支援（任意）','ご相談の流れを詳しく見る →'),
(520,'メンバー紹介・ミッション','持田 貴郁（代表理事）\n河野 良太郎（理事）\n岸 忠生（監事）\n\n制度と現場と経営をつなぎ、\n持続可能な未来を共に創る。','メンバーを詳しく見る →')]),
('私たちについて（ABOUT）',[
(520,'法人概要','法人名：一般社団法人 日本みらい医療福祉共創協会\n設立：2025年5月15日\n所在地：東京都北区赤羽1-59-8\n活動エリア：東京都・埼玉県中心、全国対応',''),
(760,'MVV・実績','MISSION：制度と現場と経営をつなぎ、持続可能な未来を共創\nVISION：地域に根ざし、全国で信頼される共創拠点\nVALUE：共に考える／現場起点／人材定着／着実な変化／誠実\n\n年間300件超の経営相談対応経験をベースに、\n経営改善・資金繰り・補助金・人材定着・事業承継を支援。',''),
(980,'メンバー詳細・連携専門家','持田 貴郁：中小企業診断士ほか多数資格\n河野 良太郎：介護ITインストラクター\n岸 忠生：IT活用・業務効率化支援\n\n医療・福祉・介護・労務・法務など\n分野別の連携専門家ネットワークで\n案件ごとに最適な支援チームを編成します。','会員・連携専門家募集を見る →')]),
('事業内容・サービス（SERVICE）',[
(980,'3軸支援メニュー','経営軸：経営計画、補助金、収益モデル再構築、M&A・承継\n人材軸：採用戦略、定着支援、管理職育成、外国人材受入\n運営軸：業務標準化、ICT・DX化、ケア品質向上、法令整備\n\n3つの軸を一体で設計し、現場で実行可能な改善へ。',''),
(760,'支援対象・料金目安','介護サービス／障がい福祉／医療・在宅医療\n保育・児童福祉／新規参入・承継検討法人\n行政・商工団体・金融機関・士業など\n\n初回相談（現状診断・課題整理）：無料\n診断レポート：50,000円（税別）〜',''),
(640,'ご相談の流れ','STEP1 事前アンケート\nSTEP2 初回面談（無料）\nSTEP3 診断レポート提出（有償）\nSTEP4 継続支援（任意）\n\n押しつけは一切しません。','無料相談はこちら →')]),
('お問い合わせ（CONTACT）',[
(620,'お問い合わせ案内','まず、話しましょう。\n下記フォームよりお気軽にお問い合わせください。\n初回相談は無料、返信は3営業日以内を目安にご連絡します。\n\n【Googleフォーム埋め込みエリア（HTML実装想定）】',''),
(980,'FAQ','Q1 初回相談は無料ですか？\nA はい、無料です。\nQ2 課題未整理でも相談できますか？\nA はい、可能です。\nQ3 全国対応できますか？\nA オンラインで全国対応可能です。\nQ4 相談後に必ず有償支援が必要ですか？\nA いいえ、任意です。\nQ5 連携専門家として関われますか？\nA はい、個別にご相談ください。',''),
(420,'個人情報の取扱い','入力いただく個人情報は、返信および当協会サービス案内のみに使用します。\n詳細はプライバシーポリシーをご確認ください。','無料相談はこちら →')]),
('プライバシーポリシー（PRIVACY）',[
(1540,'個人情報保護方針','1. 取得する個人情報：氏名、メールアドレス、電話番号、所属事業所名、お問い合わせ内容\n2. 利用目的：返信、サービス案内、講演/研修/イベント案内、事業活動連絡\n3. 第三者提供：同意時、法令に基づく場合、生命財産保護の必要時\n4. 安全管理：漏洩・滅失・毀損防止措置\n5. 開示等請求：合理的範囲で速やかに対応\n6. Cookie：利便性向上目的で使用する場合あり\n7. お問い合わせ窓口：t.mochida@mirai-welfare.com\n8. 改定：必要に応じ改定しWebで告知','')])
]

for i,(t,s) in enumerate(pages,1):
    page(t,s,f'lp_mobile_images/lp_mobile_{i:02}.svg')
print('generated',len(pages))
