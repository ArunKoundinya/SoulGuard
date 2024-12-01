# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['WebApp/SoulGuard/manage.py',
    'jupyternotebooks/mainpredictions.py',
    'jupyternotebooks/sentimentmodel.py',
    'jupyternotebooks/suicidemodel.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('WebApp/SoulGuard/myapp/templates', 'myapp/templates'),  # Correct template path
        ('WebApp/SoulGuard/static', 'static'),  # Correct static path
        ('data/worrywords-v1.csv', 'data'),
        ('data/vocab_dict.pkl', 'data'),
        ('data/suicide_detection_model.pkl', 'data'),
        ('jupyternotebooks', 'jupyternotebooks'),
    ],
    hiddenimports=['emoji','nltk','tensorflow','textblob','vaderSentiment','pysqlite2','pandas','numpy'],
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
