from eArsivPortal.Core import eArsivPortalUtils

portal = eArsivPortalUtils(
    kullanici_kodu = "3333333301",
    sifre = "1",
    test_modu      = True
)

faturalar = portal.faturalari_getir(
    baslangic_tarihi = "01/09/2023",
    bitis_tarihi     = "30/09/2023"
)

for fatura in faturalar:
    html_fatura = portal.fatura_html(
        ettn        = fatura.ettn,
        onay_durumu = fatura.onayDurumu
    )
    unvan = fatura.aliciUnvanAdSoyad
    names = unvan.split()
    if len(names) >= 2:
        name = "-".join(names[:2])
    elif names:
        name = names[0]
    else:
        print("The string is empty.")
    with open(f"{name}.html", "w", encoding="utf-8") as dosya:
        dosya.write(html_fatura)
    portal.convert_pdf(input_html=f"{name}.html", output_pdf=f"{name}.pdf", pdf_dir="Desktop/eylül")

portal.cikis_yap()