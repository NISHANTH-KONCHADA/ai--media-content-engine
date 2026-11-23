import openpyxl
from pathlib import Path

def test_completed_workbook_structure():
    wb_path = Path("submission/workbook/completed_submission_workbook.xlsx")
    assert wb_path.exists(), "Completed workbook does not exist"
    
    wb = openpyxl.load_workbook(wb_path, data_only=False)
    assert wb.sheetnames == ['00_START', '01_INSIGHT', '02_ASSETS', '03_ENGINE_LAUNCH', '04_SELF_CHECK']
    
    # Check 00_START
    ws0 = wb['00_START']
    assert ws0['B5'].value == "CB.SC.U4CSE23523"
    assert ws0['B6'].value == "K Nishanth"
    assert ws0['B7'].value == "konchadanishanth2643@gmail.com"
    assert "Amrita" in str(ws0['B8'].value)
    assert ws0['B21'].value == "Yes"
    assert ws0['B24'].value == '=COUNTIF(04_SELF_CHECK!F6:F12,"MET")&" of 7"'
    assert ws0['B25'].value == '=04_SELF_CHECK!C29'
    assert ws0['B26'].value == '=IF(B21="Yes","Yes","NOT YET")'
    assert ws0['B27'].value == '=IF(AND(COUNTIF(04_SELF_CHECK!F6:F12,"MET")=7,B21="Yes",COUNTIF(F5:F10,"Yes")=6),"YES","NOT YET - check tabs 00 and 04")'
    for r in range(5, 11):
        assert ws0[f'F{r}'].value == "Yes"

    # Check 01_INSIGHT
    ws1 = wb['01_INSIGHT']
    for r in range(6, 11):
        assert ws1[f'A{r}'].value in [1, 2, 3, 4, 5]
        assert ws1[f'B{r}'].value is not None
        assert ws1[f'E{r}'].value is not None

    for r in range(14, 17):
        assert ws1[f'A{r}'].value in [1, 2, 3]
        assert ws1[f'B{r}'].value is not None

    # Check 02_ASSETS
    ws2 = wb['02_ASSETS']
    assert ws2['A5'].value == "A001"
    assert ws2['A34'].value == "A030"
    for r in range(5, 35):
        assert ws2[f'T{r}'].value == "Ready"
        assert ws2[f'M{r}'].value == "Yes" # Rights checked
        # Check formulas preserved
        assert "COUNTIF" in str(ws2[f'V{r}'].value)
        assert "COMPLETE" in str(ws2[f'W{r}'].value)

    # Check 04_SELF_CHECK
    ws4 = wb['04_SELF_CHECK']
    assert ws4['C6'].value == 30
    assert ws4['C7'].value == 3
    assert ws4['C8'].value == 10
    assert ws4['C9'].value == 20
    assert ws4['C10'].value == 0
    assert ws4['C11'].value == "Yes"
    # Honest status: 18 qualified of 20 required participants (collection in progress)
    assert ws4['C12'].value == "No"

    assert ws4['C24'].value == 10
    assert ws4['C25'].value == 35
    assert ws4['C26'].value == 20
    assert ws4['C27'].value == 10
    assert ws4['C28'].value == 25
    assert ws4['C29'].value == '=SUM(C24:C28)'

def test_rendered_files_exist():
    assets_dir = Path("submission/content/assets")
    assert assets_dir.exists()
    
    # Check 10 short videos
    for i in range(1, 11):
        aid = f"A{i:03d}"
        v_path = assets_dir / aid / "final_video.mp4"
        s_path = assets_dir / aid / "source.json"
        assert v_path.exists(), f"Video {v_path} missing"
        assert v_path.stat().st_size > 1000, f"Video {v_path} too small"
        assert s_path.exists(), f"Source {s_path} missing"

    # Check 10 carousels
    for i in range(11, 21):
        aid = f"A{i:03d}"
        s1 = assets_dir / aid / "slide_1.png"
        s5 = assets_dir / aid / "slide_5.png"
        svg = assets_dir / aid / "source.svg"
        assert s1.exists(), f"Slide 1 missing in {aid}"
        assert s5.exists(), f"Slide 5 missing in {aid}"
        assert svg.exists(), f"Source SVG missing in {aid}"

    # Check 10 graphics
    for i in range(21, 31):
        aid = f"A{i:03d}"
        g_path = assets_dir / aid / "graphic.png"
        svg = assets_dir / aid / "source.svg"
        assert g_path.exists(), f"Graphic missing in {aid}"
        assert svg.exists(), f"Source SVG missing in {aid}"
