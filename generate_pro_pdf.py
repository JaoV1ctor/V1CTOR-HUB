import asyncio
from playwright.async_api import async_playwright
import qrcode
import base64
from io import BytesIO

# Generate QR Code for the Google Drive link
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
drive_link = "https://drive.google.com/file/d/1DsGuaP0h0r9S8XKuTOk7maKhanmvTnQm/view?usp=sharing"
qr.add_data(drive_link)
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="#050505")
buffered = BytesIO()
img.save(buffered, format="PNG")
qr_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
qr_data_uri = f"data:image/png;base64,{qr_b64}"

html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <style>
        @page {{
            size: A4;
            margin: 0;
        }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            color: #E0E0E0;
            margin: 0;
            padding: 0;
            background-color: #050505;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}
        .page {{
            width: 210mm;
            height: 297mm;
            padding: 60px 70px;
            box-sizing: border-box;
            position: relative;
            page-break-after: always;
            background-color: #050505;
            border-bottom: 1px solid #111;
        }}
        .accent {{ color: #00A3FF; }}
        .bg-accent {{ background-color: #00A3FF; }}
        
        h1 {{ font-size: 42pt; margin-bottom: 20px; font-weight: 900; line-height: 1.05; letter-spacing: -1.5px; color: #FFFFFF; }}
        h2 {{ font-size: 26pt; color: #00A3FF; margin-top: 0; font-weight: 800; margin-bottom: 25px; letter-spacing: -0.5px; }}
        h3 {{ font-size: 16pt; color: #FFFFFF; margin-top: 35px; margin-bottom: 15px; font-weight: 600; }}
        p {{ font-size: 12.5pt; line-height: 1.7; color: #A0A0A0; margin-bottom: 20px; font-weight: 400; }}
        strong {{ color: #FFFFFF; font-weight: 600; }}
        
        .hero-line {{
            width: 80px;
            height: 4px;
            background-color: #00A3FF;
            margin-bottom: 40px;
            border-radius: 2px;
        }}

        .stat-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin: 40px 0;
        }}
        .stat-item {{
            background: #0a0a0a;
            padding: 30px;
            border-left: 4px solid #00A3FF;
            border-radius: 4px;
        }}
        .stat-value {{ font-size: 28pt; font-weight: 900; color: #FFFFFF; display: block; margin-bottom: 5px; }}
        .stat-value span {{ color: #00A3FF; }}
        .stat-label {{ font-size: 10pt; color: #888; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; line-height: 1.4; display: block; }}

        .case-study {{
            background: linear-gradient(145deg, #0a0a0a 0%, #050505 100%);
            border: 1px solid #1a1a1a;
            padding: 30px;
            margin-top: 25px;
            border-radius: 8px;
        }}
        .case-tag {{
            font-size: 8.5pt;
            background: rgba(0, 163, 255, 0.1);
            color: #00A3FF;
            padding: 6px 12px;
            font-weight: 700;
            display: inline-block;
            margin-bottom: 15px;
            border-radius: 4px;
            letter-spacing: 1px;
        }}

        .methodology-list {{
            list-style: none;
            padding: 0;
            margin-top: 30px;
        }}
        .methodology-list li {{
            margin-bottom: 35px;
            border-bottom: 1px solid #151515;
            padding-bottom: 25px;
        }}
        .methodology-list li:last-child {{ border-bottom: none; }}
        .method-number {{
            font-size: 14pt;
            font-weight: 900;
            color: #00A3FF;
            margin-bottom: 10px;
            display: block;
        }}
        .method-title {{
            font-size: 16pt;
            color: #FFFFFF;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .footer {{
            position: absolute;
            bottom: 40px;
            left: 70px;
            right: 70px;
            display: flex;
            justify-content: space-between;
            font-size: 8pt;
            color: #444;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 600;
        }}

        .qr-section {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            margin-top: 50px;
            padding: 40px;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            border-radius: 12px;
        }}
        .qr-image {{
            width: 150px;
            height: 150px;
            margin-bottom: 20px;
            border-radius: 8px;
        }}
        
        .btn-link {{
            display: inline-block;
            margin-top: 30px;
            border: 1px solid #00A3FF;
            padding: 16px 45px;
            font-weight: 700;
            letter-spacing: 2px;
            color: #FFFFFF;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 10pt;
            border-radius: 4px;
        }}
    </style>
</head>
<body>

    <!-- CAPA -->
    <div class="page">
        <div style="margin-top: 150px;">
            <div class="hero-line"></div>
            <p style="text-transform: uppercase; letter-spacing: 5px; color: #00A3FF; font-weight: 800; margin-bottom: 15px; font-size: 11pt;">V1CTOR-HUB | WHITE PAPER EXCLUSIVO</p>
            <h1>O MANUAL DA<br><span class="accent">EFICIÊNCIA</span><br>DIGITAL</h1>
            <p style="max-width: 550px; font-size: 15pt; margin-top: 40px; color: #B0B0B0; font-weight: 300;">
                Por que empresas de alto crescimento não possuem apenas sites, mas <strong>ecossistemas completos de conversão e automação.</strong>
            </p>
        </div>
        <div class="footer">
            <span>JAOV1CTOR | IA & AUTOMATION BOUTIQUE</span>
            <span>ED. 2026</span>
        </div>
    </div>

    <!-- PÁGINA 2: O CONTEXTO -->
    <div class="page">
        <h2 style="margin-top: 40px;">A Morte do Site Estático</h2>
        <p>Durante as últimas duas décadas, o mercado foi ensinado que ter um "site institucional" era o suficiente para existir no ambiente digital. Hoje, essa mentalidade é o <strong>maior gargalo de receita</strong> das operações modernas.</p>
        <p>A maioria das empresas trata sua presença digital como um folheto online: estático, passivo e dependente de esforço humano para gerar qualquer resultado real.</p>
        
        <h3 style="margin-top: 50px;">O Novo Paradigma</h3>
        <p>A atenção do consumidor caiu, e a exigência por respostas imediatas subiu. Empresas que demandam preenchimento de formulários longos ou esperas de 24 horas por um e-mail estão <strong>perdendo clientes para concorrentes mais rápidos.</strong></p>
        
        <div class="stat-grid">
            <div class="stat-item">
                <span class="stat-value">3<span>s</span></span>
                <span class="stat-label">Tempo limite de carregamento antes de 40% dos usuários abandonarem a página.</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">60<span>%</span></span>
                <span class="stat-label">Redução no custo de aquisição quando se utiliza qualificação via IA.</span>
            </div>
        </div>
        
        <p>Sistemas modernos são projetados com um único foco: <strong>Reduzir a fricção.</strong> Cada pixel tem um objetivo psicológico, e cada interação é mapeada para conduzir o usuário até a conversão com o menor esforço possível.</p>
        
        <div class="footer">
            <span>PÁGINA 02</span>
            <span>O MANUAL DA EFICIÊNCIA DIGITAL</span>
        </div>
    </div>

    <!-- PÁGINA 3: METODOLOGIA -->
    <div class="page">
        <h2 style="margin-top: 40px;">A Anatomia da Alta Performance</h2>
        <p>O que separa um sistema projetado pelo <strong>V1CTOR-HUB</strong> de uma landing page comum? A resposta está na intersecção entre engenharia de software avançada e psicologia de consumo.</p>
        
        <ul class="methodology-list">
            <li>
                <span class="method-number">01.</span>
                <div class="method-title">Velocidade Extrema (Edge Computing)</div>
                <p>Sites tradicionais rodam em servidores lentos. Nós construímos aplicações baseadas em <strong>Next.js</strong> e as distribuímos em redes Edge (Vercel). Seu conteúdo é carregado instantaneamente, no servidor mais próximo do seu cliente. Resultado? Taxas de rejeição drasticamente menores.</p>
            </li>
            <li>
                <span class="method-number">02.</span>
                <div class="method-title">Agentes de Inteligência Artificial</div>
                <p>Seu sistema não pode apenas informar; ele precisa atender. Implementamos Agentes de IA que operam 24/7. Eles não usam roteiros robóticos, mas sim <strong>Processamento de Linguagem Natural</strong> para qualificar leads, tirar dúvidas complexas e agendar reuniões enquanto você dorme.</p>
            </li>
            <li>
                <span class="method-number">03.</span>
                <div class="method-title">Data-Driven UX & Neurodesign</div>
                <p>Nenhuma cor ou botão é escolhido por acaso. Aplicamos princípios de Neurodesign combinados com ferramentas de Heatmapping e Analytics. Nós mapeamos os padrões de clique e ajustamos a interface para criar um <strong>funil invisível e irresistível.</strong></p>
            </li>
        </ul>
        
        <div class="footer">
            <span>PÁGINA 03</span>
            <span>A METODOLOGIA JAOV1CTOR</span>
        </div>
    </div>

    <!-- PÁGINA 4: ESTUDOS DE CASO -->
    <div class="page">
        <h2 style="margin-top: 40px;">O Impacto no Mundo Real</h2>
        <p>A teoria da eficiência digital já foi validada pelos maiores players do mercado e, mais importante, está revolucionando negócios locais todos os dias.</p>
        
        <div class="case-study">
            <span class="case-tag">ESTUDO DE CASO GLOBAL: DOMINO'S</span>
            <div class="method-title" style="color: #fff;">A Transformação Digital da Pizza</div>
            <p>Ao mudar o foco de "vender pizza" para "criar a melhor experiência de pedido digital do mundo" (AnyWare), a Domino's viu suas ações valorizarem exponencialmente na última década. Eles automatizaram processos e criaram uma interface de alta conversão imbatível.</p>
        </div>

        <div class="case-study">
            <span class="case-tag">APLICAÇÃO LOCAL: SETOR IMOBILIÁRIO</span>
            <div class="method-title" style="color: #fff;">Aumento de Agendamentos</div>
            <p>Uma imobiliária de alto padrão perdia clientes pelo tempo de resposta aos finais de semana. A solução? Um ecossistema integrado com IA. <strong>O tempo de resposta caiu de 4 horas para 15 segundos.</strong> O resultado foi um aumento imediato de 35% no número de visitas agendadas.</p>
        </div>

        <h3 style="margin-top: 40px;">A Pergunta Central:</h3>
        <p style="font-size: 14pt; color: #FFFFFF; font-weight: 500; border-left: 3px solid #00A3FF; padding-left: 20px;">Quantos negócios você perdeu neste mês simplesmente porque o seu concorrente ofereceu uma experiência digital mais rápida, clara e automatizada?</p>
        
        <div class="footer">
            <span>PÁGINA 04</span>
            <span>ESTUDOS DE CASO</span>
        </div>
    </div>

    <!-- PÁGINA 5: CONCLUSÃO E QR CODE -->
    <div class="page" style="text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <h1 style="font-size: 32pt; margin-top: 30px;">O FUTURO É DE QUEM<br><span class="accent">AUTOMATIZA.</span></h1>
        <p style="margin-top: 20px; max-width: 600px; margin-left: auto; margin-right: auto; color: #A0A0A0;">
            O mercado não vai esperar você se adaptar. O momento de transformar o seu site em um verdadeiro motor de vendas e automação é agora.
        </p>
        
        <div style="margin: 40px auto; width: 100px; height: 3px; background: #00A3FF;"></div>
        
        <div class="qr-section">
            <h3 style="margin-top: 0; margin-bottom: 25px; color: #FFFFFF; font-size: 14pt;">ACESSE O ARQUIVO NA NUVEM</h3>
            <p style="font-size: 11pt; color: #888; max-width: 400px; margin-bottom: 25px;">
                Guarde este material. Escaneie o QR Code abaixo para acessar o PDF original hospedado em nosso Google Drive seguro:
            </p>
            <img src="{qr_data_uri}" alt="QR Code" class="qr-image" />
            <p style="font-size: 9pt; color: #666; word-break: break-all; max-width: 300px;">
                Link direto:<br> {drive_link}
            </p>
        </div>
        
        <a href="https://wa.me/5513991377983?text=Quero%20agendar%20meu%20diagnóstico%20gratuito%20de%2015%20minutos." class="btn-link">
            AGENDAR DIAGNÓSTICO GRATUITO
        </a>
        
        <div class="footer" style="justify-content: center;">
            <span>DOCUMENTO CONFIDENCIAL | USO EXCLUSIVO V1CTOR-HUB</span>
        </div>
    </div>

</body>
</html>
"""

async def generate_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.pdf(
            path="Manual_Eficiencia_Digital_JaoV1ctor_PRO.pdf", 
            format="A4", 
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        await browser.close()

asyncio.run(generate_pdf())
