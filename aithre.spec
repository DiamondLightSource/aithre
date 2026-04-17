# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ['bin/guiv4_prod.py'],
    pathex=['bin'],
    binaries=[],
    datas=[
        ('bin/guiv4_3_0.ui', 'bin'),
        ('guiv4.ui', '.'),
        ('bin/icon.png', 'bin'),
        ('bin/up.png', 'bin'),
        ('bin/down.png', 'bin'),
        ('bin/left.png', 'bin'),
        ('bin/right.png', 'bin'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'bluesky',
        'ophyd',
        'ophyd_async',
        'softioc',
        'mx_bluesky',
        'dodal',
        'blueapi',
        'rtc6_fastcs',
        'IPython',
        'tkinter',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='aithre',
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
    icon='bin/icon.png',
)
