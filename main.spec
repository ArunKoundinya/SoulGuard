# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py',
    'jupyternotebooks/mainpredictions.py',
    'jupyternotebooks/sentimentmodel.py',
    'jupyternotebooks/suicidemodel.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('WebApp/SoulGuard/manage.py', 'WebApp/SoulGuard'),  # Include manage.py
        ('WebApp/SoulGuard/soul/settings.py', 'WebApp/SoulGuard/soul'),  # Include settings
        ('WebApp/SoulGuard/myapp/Templates', 'WebApp/SoulGuard/myapp/Templates'),  # Include templates folder
        ('WebApp/SoulGuard/static', 'WebApp/SoulGuard/static'),  # Include static files
        ('data/worrywords-v1.csv', 'data'),
        ('data/vocab_dict.pkl', 'data'),
        ('data/suicide_detection_model.pkl', 'data'),
    ],
    hiddenimports=['emoji','nltk','tensorflow','textblob','vaderSentiment'],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
