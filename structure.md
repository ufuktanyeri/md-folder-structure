```md
camera-monitoring-system/
├── .env/
└── README.md
├── assets/
├── docs/
└── main.py
└── requirements.txt
├── src/
│   ├── config/
│   │   └── camera_config.jsonc
│   ├── modules/
│   │   ├── __pycache__/
│   │   │   └── rtsp_viewer.cpython-313.pyc
│   │   └── rtsp_viewer.py
│   ├── services/
│   ├── ui/
│   ├── utils/
├── tests/
├── venv/
│   └── .gitignore
│   ├── Include/
│   ├── Lib/
│   │   ├── site-packages/
│   │   │   ├── MarkupSafe-3.0.2.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── PIL/
│   │   │   │   └── BdfFontFile.py
│   │   │   │   └── BlpImagePlugin.py
│   │   │   │   └── BmpImagePlugin.py
│   │   │   │   └── BufrStubImagePlugin.py
│   │   │   │   └── ContainerIO.py
│   │   │   │   └── CurImagePlugin.py
│   │   │   │   └── DcxImagePlugin.py
│   │   │   │   └── DdsImagePlugin.py
│   │   │   │   └── EpsImagePlugin.py
│   │   │   │   └── ExifTags.py
│   │   │   │   └── FitsImagePlugin.py
│   │   │   │   └── FliImagePlugin.py
│   │   │   │   └── FontFile.py
│   │   │   │   └── FpxImagePlugin.py
│   │   │   │   └── FtexImagePlugin.py
│   │   │   │   └── GbrImagePlugin.py
│   │   │   │   └── GdImageFile.py
│   │   │   │   └── GifImagePlugin.py
│   │   │   │   └── GimpGradientFile.py
│   │   │   │   └── GimpPaletteFile.py
│   │   │   │   └── GribStubImagePlugin.py
│   │   │   │   └── Hdf5StubImagePlugin.py
│   │   │   │   └── IcnsImagePlugin.py
│   │   │   │   └── IcoImagePlugin.py
│   │   │   │   └── ImImagePlugin.py
│   │   │   │   └── Image.py
│   │   │   │   └── ImageChops.py
│   │   │   │   └── ImageCms.py
│   │   │   │   └── ImageColor.py
│   │   │   │   └── ImageDraw.py
│   │   │   │   └── ImageDraw2.py
│   │   │   │   └── ImageEnhance.py
│   │   │   │   └── ImageFile.py
│   │   │   │   └── ImageFilter.py
│   │   │   │   └── ImageFont.py
│   │   │   │   └── ImageGrab.py
│   │   │   │   └── ImageMath.py
│   │   │   │   └── ImageMode.py
│   │   │   │   └── ImageMorph.py
│   │   │   │   └── ImageOps.py
│   │   │   │   └── ImagePalette.py
│   │   │   │   └── ImagePath.py
│   │   │   │   └── ImageQt.py
│   │   │   │   └── ImageSequence.py
│   │   │   │   └── ImageShow.py
│   │   │   │   └── ImageStat.py
│   │   │   │   └── ImageTk.py
│   │   │   │   └── ImageTransform.py
│   │   │   │   └── ImageWin.py
│   │   │   │   └── ImtImagePlugin.py
│   │   │   │   └── IptcImagePlugin.py
│   │   │   │   └── Jpeg2KImagePlugin.py
│   │   │   │   └── JpegImagePlugin.py
│   │   │   │   └── JpegPresets.py
│   │   │   │   └── McIdasImagePlugin.py
│   │   │   │   └── MicImagePlugin.py
│   │   │   │   └── MpegImagePlugin.py
│   │   │   │   └── MpoImagePlugin.py
│   │   │   │   └── MspImagePlugin.py
│   │   │   │   └── PSDraw.py
│   │   │   │   └── PaletteFile.py
│   │   │   │   └── PalmImagePlugin.py
│   │   │   │   └── PcdImagePlugin.py
│   │   │   │   └── PcfFontFile.py
│   │   │   │   └── PcxImagePlugin.py
│   │   │   │   └── PdfImagePlugin.py
│   │   │   │   └── PdfParser.py
│   │   │   │   └── PixarImagePlugin.py
│   │   │   │   └── PngImagePlugin.py
│   │   │   │   └── PpmImagePlugin.py
│   │   │   │   └── PsdImagePlugin.py
│   │   │   │   └── QoiImagePlugin.py
│   │   │   │   └── SgiImagePlugin.py
│   │   │   │   └── SpiderImagePlugin.py
│   │   │   │   └── SunImagePlugin.py
│   │   │   │   └── TarIO.py
│   │   │   │   └── TgaImagePlugin.py
│   │   │   │   └── TiffImagePlugin.py
│   │   │   │   └── TiffTags.py
│   │   │   │   └── WalImageFile.py
│   │   │   │   └── WebPImagePlugin.py
│   │   │   │   └── WmfImagePlugin.py
│   │   │   │   └── XVThumbImagePlugin.py
│   │   │   │   └── XbmImagePlugin.py
│   │   │   │   └── XpmImagePlugin.py
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── BdfFontFile.cpython-313.pyc
│   │   │   │   │   └── BlpImagePlugin.cpython-313.pyc
│   │   │   │   │   └── BmpImagePlugin.cpython-313.pyc
│   │   │   │   │   └── BufrStubImagePlugin.cpython-313.pyc
│   │   │   │   │   └── ContainerIO.cpython-313.pyc
│   │   │   │   │   └── CurImagePlugin.cpython-313.pyc
│   │   │   │   │   └── DcxImagePlugin.cpython-313.pyc
│   │   │   │   │   └── DdsImagePlugin.cpython-313.pyc
│   │   │   │   │   └── EpsImagePlugin.cpython-313.pyc
│   │   │   │   │   └── ExifTags.cpython-313.pyc
│   │   │   │   │   └── FitsImagePlugin.cpython-313.pyc
│   │   │   │   │   └── FliImagePlugin.cpython-313.pyc
│   │   │   │   │   └── FontFile.cpython-313.pyc
│   │   │   │   │   └── FpxImagePlugin.cpython-313.pyc
│   │   │   │   │   └── FtexImagePlugin.cpython-313.pyc
│   │   │   │   │   └── GbrImagePlugin.cpython-313.pyc
│   │   │   │   │   └── GdImageFile.cpython-313.pyc
│   │   │   │   │   └── GifImagePlugin.cpython-313.pyc
│   │   │   │   │   └── GimpGradientFile.cpython-313.pyc
│   │   │   │   │   └── GimpPaletteFile.cpython-313.pyc
│   │   │   │   │   └── GribStubImagePlugin.cpython-313.pyc
│   │   │   │   │   └── Hdf5StubImagePlugin.cpython-313.pyc
│   │   │   │   │   └── IcnsImagePlugin.cpython-313.pyc
│   │   │   │   │   └── IcoImagePlugin.cpython-313.pyc
│   │   │   │   │   └── ImImagePlugin.cpython-313.pyc
│   │   │   │   │   └── Image.cpython-313.pyc
│   │   │   │   │   └── ImageChops.cpython-313.pyc
│   │   │   │   │   └── ImageCms.cpython-313.pyc
│   │   │   │   │   └── ImageColor.cpython-313.pyc
│   │   │   │   │   └── ImageDraw.cpython-313.pyc
│   │   │   │   │   └── ImageDraw2.cpython-313.pyc
│   │   │   │   │   └── ImageEnhance.cpython-313.pyc
│   │   │   │   │   └── ImageFile.cpython-313.pyc
│   │   │   │   │   └── ImageFilter.cpython-313.pyc
│   │   │   │   │   └── ImageFont.cpython-313.pyc
│   │   │   │   │   └── ImageGrab.cpython-313.pyc
│   │   │   │   │   └── ImageMath.cpython-313.pyc
│   │   │   │   │   └── ImageMode.cpython-313.pyc
│   │   │   │   │   └── ImageMorph.cpython-313.pyc
│   │   │   │   │   └── ImageOps.cpython-313.pyc
│   │   │   │   │   └── ImagePalette.cpython-313.pyc
│   │   │   │   │   └── ImagePath.cpython-313.pyc
│   │   │   │   │   └── ImageQt.cpython-313.pyc
│   │   │   │   │   └── ImageSequence.cpython-313.pyc
│   │   │   │   │   └── ImageShow.cpython-313.pyc
│   │   │   │   │   └── ImageStat.cpython-313.pyc
│   │   │   │   │   └── ImageTk.cpython-313.pyc
│   │   │   │   │   └── ImageTransform.cpython-313.pyc
│   │   │   │   │   └── ImageWin.cpython-313.pyc
│   │   │   │   │   └── ImtImagePlugin.cpython-313.pyc
│   │   │   │   │   └── IptcImagePlugin.cpython-313.pyc
│   │   │   │   │   └── Jpeg2KImagePlugin.cpython-313.pyc
│   │   │   │   │   └── JpegImagePlugin.cpython-313.pyc
│   │   │   │   │   └── JpegPresets.cpython-313.pyc
│   │   │   │   │   └── McIdasImagePlugin.cpython-313.pyc
│   │   │   │   │   └── MicImagePlugin.cpython-313.pyc
│   │   │   │   │   └── MpegImagePlugin.cpython-313.pyc
│   │   │   │   │   └── MpoImagePlugin.cpython-313.pyc
│   │   │   │   │   └── MspImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PSDraw.cpython-313.pyc
│   │   │   │   │   └── PaletteFile.cpython-313.pyc
│   │   │   │   │   └── PalmImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PcdImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PcfFontFile.cpython-313.pyc
│   │   │   │   │   └── PcxImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PdfImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PdfParser.cpython-313.pyc
│   │   │   │   │   └── PixarImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PngImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PpmImagePlugin.cpython-313.pyc
│   │   │   │   │   └── PsdImagePlugin.cpython-313.pyc
│   │   │   │   │   └── QoiImagePlugin.cpython-313.pyc
│   │   │   │   │   └── SgiImagePlugin.cpython-313.pyc
│   │   │   │   │   └── SpiderImagePlugin.cpython-313.pyc
│   │   │   │   │   └── SunImagePlugin.cpython-313.pyc
│   │   │   │   │   └── TarIO.cpython-313.pyc
│   │   │   │   │   └── TgaImagePlugin.cpython-313.pyc
│   │   │   │   │   └── TiffImagePlugin.cpython-313.pyc
│   │   │   │   │   └── TiffTags.cpython-313.pyc
│   │   │   │   │   └── WalImageFile.cpython-313.pyc
│   │   │   │   │   └── WebPImagePlugin.cpython-313.pyc
│   │   │   │   │   └── WmfImagePlugin.cpython-313.pyc
│   │   │   │   │   └── XVThumbImagePlugin.cpython-313.pyc
│   │   │   │   │   └── XbmImagePlugin.cpython-313.pyc
│   │   │   │   │   └── XpmImagePlugin.cpython-313.pyc
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── _binary.cpython-313.pyc
│   │   │   │   │   └── _deprecate.cpython-313.pyc
│   │   │   │   │   └── _tkinter_finder.cpython-313.pyc
│   │   │   │   │   └── _typing.cpython-313.pyc
│   │   │   │   │   └── _util.cpython-313.pyc
│   │   │   │   │   └── _version.cpython-313.pyc
│   │   │   │   │   └── features.cpython-313.pyc
│   │   │   │   │   └── report.cpython-313.pyc
│   │   │   │   └── _binary.py
│   │   │   │   └── _deprecate.py
│   │   │   │   └── _imaging.cp313-win_amd64.pyd
│   │   │   │   └── _imaging.pyi
│   │   │   │   └── _imagingcms.cp313-win_amd64.pyd
│   │   │   │   └── _imagingcms.pyi
│   │   │   │   └── _imagingft.cp313-win_amd64.pyd
│   │   │   │   └── _imagingft.pyi
│   │   │   │   └── _imagingmath.cp313-win_amd64.pyd
│   │   │   │   └── _imagingmath.pyi
│   │   │   │   └── _imagingmorph.cp313-win_amd64.pyd
│   │   │   │   └── _imagingmorph.pyi
│   │   │   │   └── _imagingtk.cp313-win_amd64.pyd
│   │   │   │   └── _imagingtk.pyi
│   │   │   │   └── _tkinter_finder.py
│   │   │   │   └── _typing.py
│   │   │   │   └── _util.py
│   │   │   │   └── _version.py
│   │   │   │   └── _webp.cp313-win_amd64.pyd
│   │   │   │   └── _webp.pyi
│   │   │   │   └── features.py
│   │   │   │   └── py.typed
│   │   │   │   └── report.py
│   │   │   ├── __pycache__/
│   │   │   │   └── requests_file.cpython-313.pyc
│   │   │   ├── attr/
│   │   │   │   └── __init__.py
│   │   │   │   └── __init__.pyi
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _cmp.cpython-313.pyc
│   │   │   │   │   └── _compat.cpython-313.pyc
│   │   │   │   │   └── _config.cpython-313.pyc
│   │   │   │   │   └── _funcs.cpython-313.pyc
│   │   │   │   │   └── _make.cpython-313.pyc
│   │   │   │   │   └── _next_gen.cpython-313.pyc
│   │   │   │   │   └── _version_info.cpython-313.pyc
│   │   │   │   │   └── converters.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── filters.cpython-313.pyc
│   │   │   │   │   └── setters.cpython-313.pyc
│   │   │   │   │   └── validators.cpython-313.pyc
│   │   │   │   └── _cmp.py
│   │   │   │   └── _cmp.pyi
│   │   │   │   └── _compat.py
│   │   │   │   └── _config.py
│   │   │   │   └── _funcs.py
│   │   │   │   └── _make.py
│   │   │   │   └── _next_gen.py
│   │   │   │   └── _typing_compat.pyi
│   │   │   │   └── _version_info.py
│   │   │   │   └── _version_info.pyi
│   │   │   │   └── converters.py
│   │   │   │   └── converters.pyi
│   │   │   │   └── exceptions.py
│   │   │   │   └── exceptions.pyi
│   │   │   │   └── filters.py
│   │   │   │   └── filters.pyi
│   │   │   │   └── py.typed
│   │   │   │   └── setters.py
│   │   │   │   └── setters.pyi
│   │   │   │   └── validators.py
│   │   │   │   └── validators.pyi
│   │   │   ├── attrs/
│   │   │   │   └── __init__.py
│   │   │   │   └── __init__.pyi
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── converters.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── filters.cpython-313.pyc
│   │   │   │   │   └── setters.cpython-313.pyc
│   │   │   │   │   └── validators.cpython-313.pyc
│   │   │   │   └── converters.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── filters.py
│   │   │   │   └── py.typed
│   │   │   │   └── setters.py
│   │   │   │   └── validators.py
│   │   │   ├── attrs-25.3.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE
│   │   │   ├── blinker/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _utilities.cpython-313.pyc
│   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   └── _utilities.py
│   │   │   │   └── base.py
│   │   │   │   └── py.typed
│   │   │   ├── blinker-1.9.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   ├── certifi/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── core.cpython-313.pyc
│   │   │   │   └── cacert.pem
│   │   │   │   └── core.py
│   │   │   │   └── py.typed
│   │   │   ├── certifi-2025.1.31.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── charset_normalizer/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── api.cpython-313.pyc
│   │   │   │   │   └── cd.cpython-313.pyc
│   │   │   │   │   └── constant.cpython-313.pyc
│   │   │   │   │   └── legacy.cpython-313.pyc
│   │   │   │   │   └── md.cpython-313.pyc
│   │   │   │   │   └── models.cpython-313.pyc
│   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   └── api.py
│   │   │   │   └── cd.py
│   │   │   │   ├── cli/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __main__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   └── constant.py
│   │   │   │   └── legacy.py
│   │   │   │   └── md.cp313-win_amd64.pyd
│   │   │   │   └── md.py
│   │   │   │   └── md__mypyc.cp313-win_amd64.pyd
│   │   │   │   └── models.py
│   │   │   │   └── py.typed
│   │   │   │   └── utils.py
│   │   │   │   └── version.py
│   │   │   ├── charset_normalizer-3.4.1.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   │   └── top_level.txt
│   │   │   ├── click/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _compat.cpython-313.pyc
│   │   │   │   │   └── _termui_impl.cpython-313.pyc
│   │   │   │   │   └── _textwrap.cpython-313.pyc
│   │   │   │   │   └── _winconsole.cpython-313.pyc
│   │   │   │   │   └── core.cpython-313.pyc
│   │   │   │   │   └── decorators.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── formatting.cpython-313.pyc
│   │   │   │   │   └── globals.cpython-313.pyc
│   │   │   │   │   └── parser.cpython-313.pyc
│   │   │   │   │   └── shell_completion.cpython-313.pyc
│   │   │   │   │   └── termui.cpython-313.pyc
│   │   │   │   │   └── testing.cpython-313.pyc
│   │   │   │   │   └── types.cpython-313.pyc
│   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   └── _compat.py
│   │   │   │   └── _termui_impl.py
│   │   │   │   └── _textwrap.py
│   │   │   │   └── _winconsole.py
│   │   │   │   └── core.py
│   │   │   │   └── decorators.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── formatting.py
│   │   │   │   └── globals.py
│   │   │   │   └── parser.py
│   │   │   │   └── py.typed
│   │   │   │   └── shell_completion.py
│   │   │   │   └── termui.py
│   │   │   │   └── testing.py
│   │   │   │   └── types.py
│   │   │   │   └── utils.py
│   │   │   ├── click-8.1.8.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   ├── colorama/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── ansi.cpython-313.pyc
│   │   │   │   │   └── ansitowin32.cpython-313.pyc
│   │   │   │   │   └── initialise.cpython-313.pyc
│   │   │   │   │   └── win32.cpython-313.pyc
│   │   │   │   │   └── winterm.cpython-313.pyc
│   │   │   │   └── ansi.py
│   │   │   │   └── ansitowin32.py
│   │   │   │   └── initialise.py
│   │   │   │   ├── tests/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── ansi_test.cpython-313.pyc
│   │   │   │   │   │   └── ansitowin32_test.cpython-313.pyc
│   │   │   │   │   │   └── initialise_test.cpython-313.pyc
│   │   │   │   │   │   └── isatty_test.cpython-313.pyc
│   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   └── winterm_test.cpython-313.pyc
│   │   │   │   │   └── ansi_test.py
│   │   │   │   │   └── ansitowin32_test.py
│   │   │   │   │   └── initialise_test.py
│   │   │   │   │   └── isatty_test.py
│   │   │   │   │   └── utils.py
│   │   │   │   │   └── winterm_test.py
│   │   │   │   └── win32.py
│   │   │   │   └── winterm.py
│   │   │   ├── colorama-0.4.6.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE.txt
│   │   │   ├── cv2/
│   │   │   │   ├── Error/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   └── LICENSE-3RD-PARTY.txt
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── __init__.py
│   │   │   │   └── __init__.pyi
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── config-3.cpython-313.pyc
│   │   │   │   │   └── config.cpython-313.pyc
│   │   │   │   │   └── load_config_py2.cpython-313.pyc
│   │   │   │   │   └── load_config_py3.cpython-313.pyc
│   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   ├── aruco/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── barcode/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   └── config-3.py
│   │   │   │   └── config.py
│   │   │   │   ├── cuda/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   └── cv2.pyd
│   │   │   │   ├── data/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── haarcascade_eye.xml
│   │   │   │   │   └── haarcascade_eye_tree_eyeglasses.xml
│   │   │   │   │   └── haarcascade_frontalcatface.xml
│   │   │   │   │   └── haarcascade_frontalcatface_extended.xml
│   │   │   │   │   └── haarcascade_frontalface_alt.xml
│   │   │   │   │   └── haarcascade_frontalface_alt2.xml
│   │   │   │   │   └── haarcascade_frontalface_alt_tree.xml
│   │   │   │   │   └── haarcascade_frontalface_default.xml
│   │   │   │   │   └── haarcascade_fullbody.xml
│   │   │   │   │   └── haarcascade_lefteye_2splits.xml
│   │   │   │   │   └── haarcascade_license_plate_rus_16stages.xml
│   │   │   │   │   └── haarcascade_lowerbody.xml
│   │   │   │   │   └── haarcascade_profileface.xml
│   │   │   │   │   └── haarcascade_righteye_2splits.xml
│   │   │   │   │   └── haarcascade_russian_plate_number.xml
│   │   │   │   │   └── haarcascade_smile.xml
│   │   │   │   │   └── haarcascade_upperbody.xml
│   │   │   │   ├── detail/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── dnn/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── fisheye/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── flann/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── gapi/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   ├── core/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── cpu/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── fluid/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── ocl/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── ie/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── detail/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── imgproc/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── fluid/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── oak/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── onnx/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── ep/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── ot/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── cpu/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── ov/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── own/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── detail/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── render/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── ocv/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── streaming/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── video/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── wip/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── draw/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── gst/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── onevpl/
│   │   │   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── ipp/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   └── load_config_py2.py
│   │   │   │   └── load_config_py3.py
│   │   │   │   ├── mat_wrapper/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   ├── misc/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   │   └── version.py
│   │   │   │   ├── ml/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── ocl/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── ogl/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   └── opencv_videoio_ffmpeg4110_64.dll
│   │   │   │   ├── parallel/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   └── py.typed
│   │   │   │   ├── samples/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── segmentation/
│   │   │   │   │   └── __init__.pyi
│   │   │   │   ├── typing/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   ├── utils/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   ├── fs/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── nested/
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   └── version.py
│   │   │   │   ├── videoio_registry/
│   │   │   │   │   └── __init__.pyi
│   │   │   ├── dotenv/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── cli.cpython-313.pyc
│   │   │   │   │   └── ipython.cpython-313.pyc
│   │   │   │   │   └── main.cpython-313.pyc
│   │   │   │   │   └── parser.cpython-313.pyc
│   │   │   │   │   └── variables.cpython-313.pyc
│   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   └── cli.py
│   │   │   │   └── ipython.py
│   │   │   │   └── main.py
│   │   │   │   └── parser.py
│   │   │   │   └── py.typed
│   │   │   │   └── variables.py
│   │   │   │   └── version.py
│   │   │   ├── flask/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── app.cpython-313.pyc
│   │   │   │   │   └── blueprints.cpython-313.pyc
│   │   │   │   │   └── cli.cpython-313.pyc
│   │   │   │   │   └── config.cpython-313.pyc
│   │   │   │   │   └── ctx.cpython-313.pyc
│   │   │   │   │   └── debughelpers.cpython-313.pyc
│   │   │   │   │   └── globals.cpython-313.pyc
│   │   │   │   │   └── helpers.cpython-313.pyc
│   │   │   │   │   └── logging.cpython-313.pyc
│   │   │   │   │   └── sessions.cpython-313.pyc
│   │   │   │   │   └── signals.cpython-313.pyc
│   │   │   │   │   └── templating.cpython-313.pyc
│   │   │   │   │   └── testing.cpython-313.pyc
│   │   │   │   │   └── typing.cpython-313.pyc
│   │   │   │   │   └── views.cpython-313.pyc
│   │   │   │   │   └── wrappers.cpython-313.pyc
│   │   │   │   └── app.py
│   │   │   │   └── blueprints.py
│   │   │   │   └── cli.py
│   │   │   │   └── config.py
│   │   │   │   └── ctx.py
│   │   │   │   └── debughelpers.py
│   │   │   │   └── globals.py
│   │   │   │   └── helpers.py
│   │   │   │   ├── json/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── provider.cpython-313.pyc
│   │   │   │   │   │   └── tag.cpython-313.pyc
│   │   │   │   │   └── provider.py
│   │   │   │   │   └── tag.py
│   │   │   │   └── logging.py
│   │   │   │   └── py.typed
│   │   │   │   ├── sansio/
│   │   │   │   │   └── README.md
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── app.cpython-313.pyc
│   │   │   │   │   │   └── blueprints.cpython-313.pyc
│   │   │   │   │   │   └── scaffold.cpython-313.pyc
│   │   │   │   │   └── app.py
│   │   │   │   │   └── blueprints.py
│   │   │   │   │   └── scaffold.py
│   │   │   │   └── sessions.py
│   │   │   │   └── signals.py
│   │   │   │   └── templating.py
│   │   │   │   └── testing.py
│   │   │   │   └── typing.py
│   │   │   │   └── views.py
│   │   │   │   └── wrappers.py
│   │   │   ├── flask-3.1.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   ├── idna/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── codec.cpython-313.pyc
│   │   │   │   │   └── compat.cpython-313.pyc
│   │   │   │   │   └── core.cpython-313.pyc
│   │   │   │   │   └── idnadata.cpython-313.pyc
│   │   │   │   │   └── intranges.cpython-313.pyc
│   │   │   │   │   └── package_data.cpython-313.pyc
│   │   │   │   │   └── uts46data.cpython-313.pyc
│   │   │   │   └── codec.py
│   │   │   │   └── compat.py
│   │   │   │   └── core.py
│   │   │   │   └── idnadata.py
│   │   │   │   └── intranges.py
│   │   │   │   └── package_data.py
│   │   │   │   └── py.typed
│   │   │   │   └── uts46data.py
│   │   │   ├── idna-3.10.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.md
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   ├── isodate/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── duration.cpython-313.pyc
│   │   │   │   │   └── isodates.cpython-313.pyc
│   │   │   │   │   └── isodatetime.cpython-313.pyc
│   │   │   │   │   └── isoduration.cpython-313.pyc
│   │   │   │   │   └── isoerror.cpython-313.pyc
│   │   │   │   │   └── isostrf.cpython-313.pyc
│   │   │   │   │   └── isotime.cpython-313.pyc
│   │   │   │   │   └── isotzinfo.cpython-313.pyc
│   │   │   │   │   └── tzinfo.cpython-313.pyc
│   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   └── duration.py
│   │   │   │   └── isodates.py
│   │   │   │   └── isodatetime.py
│   │   │   │   └── isoduration.py
│   │   │   │   └── isoerror.py
│   │   │   │   └── isostrf.py
│   │   │   │   └── isotime.py
│   │   │   │   └── isotzinfo.py
│   │   │   │   └── tzinfo.py
│   │   │   │   └── version.py
│   │   │   ├── isodate-0.7.2.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── itsdangerous/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _json.cpython-313.pyc
│   │   │   │   │   └── encoding.cpython-313.pyc
│   │   │   │   │   └── exc.cpython-313.pyc
│   │   │   │   │   └── serializer.cpython-313.pyc
│   │   │   │   │   └── signer.cpython-313.pyc
│   │   │   │   │   └── timed.cpython-313.pyc
│   │   │   │   │   └── url_safe.cpython-313.pyc
│   │   │   │   └── _json.py
│   │   │   │   └── encoding.py
│   │   │   │   └── exc.py
│   │   │   │   └── py.typed
│   │   │   │   └── serializer.py
│   │   │   │   └── signer.py
│   │   │   │   └── timed.py
│   │   │   │   └── url_safe.py
│   │   │   ├── itsdangerous-2.2.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   ├── jinja2/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _identifier.cpython-313.pyc
│   │   │   │   │   └── async_utils.cpython-313.pyc
│   │   │   │   │   └── bccache.cpython-313.pyc
│   │   │   │   │   └── compiler.cpython-313.pyc
│   │   │   │   │   └── constants.cpython-313.pyc
│   │   │   │   │   └── debug.cpython-313.pyc
│   │   │   │   │   └── defaults.cpython-313.pyc
│   │   │   │   │   └── environment.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── ext.cpython-313.pyc
│   │   │   │   │   └── filters.cpython-313.pyc
│   │   │   │   │   └── idtracking.cpython-313.pyc
│   │   │   │   │   └── lexer.cpython-313.pyc
│   │   │   │   │   └── loaders.cpython-313.pyc
│   │   │   │   │   └── meta.cpython-313.pyc
│   │   │   │   │   └── nativetypes.cpython-313.pyc
│   │   │   │   │   └── nodes.cpython-313.pyc
│   │   │   │   │   └── optimizer.cpython-313.pyc
│   │   │   │   │   └── parser.cpython-313.pyc
│   │   │   │   │   └── runtime.cpython-313.pyc
│   │   │   │   │   └── sandbox.cpython-313.pyc
│   │   │   │   │   └── tests.cpython-313.pyc
│   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   └── visitor.cpython-313.pyc
│   │   │   │   └── _identifier.py
│   │   │   │   └── async_utils.py
│   │   │   │   └── bccache.py
│   │   │   │   └── compiler.py
│   │   │   │   └── constants.py
│   │   │   │   └── debug.py
│   │   │   │   └── defaults.py
│   │   │   │   └── environment.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── ext.py
│   │   │   │   └── filters.py
│   │   │   │   └── idtracking.py
│   │   │   │   └── lexer.py
│   │   │   │   └── loaders.py
│   │   │   │   └── meta.py
│   │   │   │   └── nativetypes.py
│   │   │   │   └── nodes.py
│   │   │   │   └── optimizer.py
│   │   │   │   └── parser.py
│   │   │   │   └── py.typed
│   │   │   │   └── runtime.py
│   │   │   │   └── sandbox.py
│   │   │   │   └── tests.py
│   │   │   │   └── utils.py
│   │   │   │   └── visitor.py
│   │   │   ├── jinja2-3.1.6.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE.txt
│   │   │   ├── json_spec-0.12.0.dist-info/
│   │   │   │   └── AUTHORS
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   ├── jsoncomment/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── comments.cpython-313.pyc
│   │   │   │   │   └── wrapper.cpython-313.pyc
│   │   │   │   └── comments.py
│   │   │   │   └── wrapper.py
│   │   │   ├── jsoncomment-0.4.2.dist-info/
│   │   │   │   └── COPYING
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── jsonspec/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── _compat.cpython-313.pyc
│   │   │   │   │   └── cli.cpython-313.pyc
│   │   │   │   │   └── driver.cpython-313.pyc
│   │   │   │   └── _compat.py
│   │   │   │   └── cli.py
│   │   │   │   └── driver.py
│   │   │   │   ├── misc/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   ├── schemas/
│   │   │   │   │   │   └── address.json
│   │   │   │   │   │   └── calendar.json
│   │   │   │   │   │   ├── draft-03/
│   │   │   │   │   │   │   └── card.json
│   │   │   │   │   │   │   └── hyper-schema.json
│   │   │   │   │   │   │   └── json-ref.json
│   │   │   │   │   │   │   └── links.json
│   │   │   │   │   │   │   └── schema.json
│   │   │   │   │   │   ├── draft-04/
│   │   │   │   │   │   │   └── hyper-schema.json
│   │   │   │   │   │   │   └── schema.json
│   │   │   │   │   │   └── geo.json
│   │   │   │   ├── operations/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── bases.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── bases.py
│   │   │   │   │   └── exceptions.py
│   │   │   │   ├── pointer/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── bases.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   └── stages.cpython-313.pyc
│   │   │   │   │   └── bases.py
│   │   │   │   │   └── exceptions.py
│   │   │   │   │   └── stages.py
│   │   │   │   ├── reference/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── bases.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   └── providers.cpython-313.pyc
│   │   │   │   │   │   └── util.cpython-313.pyc
│   │   │   │   │   └── bases.py
│   │   │   │   │   └── exceptions.py
│   │   │   │   │   └── providers.py
│   │   │   │   │   └── util.py
│   │   │   │   ├── validators/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── bases.cpython-313.pyc
│   │   │   │   │   │   └── draft03.cpython-313.pyc
│   │   │   │   │   │   └── draft04.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   └── factorize.cpython-313.pyc
│   │   │   │   │   │   └── formats.cpython-313.pyc
│   │   │   │   │   │   └── pointer_util.cpython-313.pyc
│   │   │   │   │   │   └── util.cpython-313.pyc
│   │   │   │   │   └── bases.py
│   │   │   │   │   └── draft03.py
│   │   │   │   │   └── draft04.py
│   │   │   │   │   └── exceptions.py
│   │   │   │   │   └── factorize.py
│   │   │   │   │   └── formats.py
│   │   │   │   │   └── pointer_util.py
│   │   │   │   │   └── util.py
│   │   │   ├── lxml/
│   │   │   │   └── ElementInclude.py
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── ElementInclude.cpython-313.pyc
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _elementpath.cpython-313.pyc
│   │   │   │   │   └── builder.cpython-313.pyc
│   │   │   │   │   └── cssselect.cpython-313.pyc
│   │   │   │   │   └── doctestcompare.cpython-313.pyc
│   │   │   │   │   └── pyclasslookup.cpython-313.pyc
│   │   │   │   │   └── sax.cpython-313.pyc
│   │   │   │   │   └── usedoctest.cpython-313.pyc
│   │   │   │   └── _elementpath.cp313-win_amd64.pyd
│   │   │   │   └── _elementpath.py
│   │   │   │   └── apihelpers.pxi
│   │   │   │   └── builder.cp313-win_amd64.pyd
│   │   │   │   └── builder.py
│   │   │   │   └── classlookup.pxi
│   │   │   │   └── cleanup.pxi
│   │   │   │   └── cssselect.py
│   │   │   │   └── debug.pxi
│   │   │   │   └── docloader.pxi
│   │   │   │   └── doctestcompare.py
│   │   │   │   └── dtd.pxi
│   │   │   │   └── etree.cp313-win_amd64.pyd
│   │   │   │   └── etree.h
│   │   │   │   └── etree.pyx
│   │   │   │   └── etree_api.h
│   │   │   │   └── extensions.pxi
│   │   │   │   ├── html/
│   │   │   │   │   └── ElementSoup.py
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── ElementSoup.cpython-313.pyc
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _diffcommand.cpython-313.pyc
│   │   │   │   │   │   └── _html5builder.cpython-313.pyc
│   │   │   │   │   │   └── _setmixin.cpython-313.pyc
│   │   │   │   │   │   └── builder.cpython-313.pyc
│   │   │   │   │   │   └── clean.cpython-313.pyc
│   │   │   │   │   │   └── defs.cpython-313.pyc
│   │   │   │   │   │   └── diff.cpython-313.pyc
│   │   │   │   │   │   └── formfill.cpython-313.pyc
│   │   │   │   │   │   └── html5parser.cpython-313.pyc
│   │   │   │   │   │   └── soupparser.cpython-313.pyc
│   │   │   │   │   │   └── usedoctest.cpython-313.pyc
│   │   │   │   │   └── _diffcommand.py
│   │   │   │   │   └── _html5builder.py
│   │   │   │   │   └── _setmixin.py
│   │   │   │   │   └── builder.py
│   │   │   │   │   └── clean.py
│   │   │   │   │   └── defs.py
│   │   │   │   │   └── diff.cp313-win_amd64.pyd
│   │   │   │   │   └── diff.py
│   │   │   │   │   └── formfill.py
│   │   │   │   │   └── html5parser.py
│   │   │   │   │   └── soupparser.py
│   │   │   │   │   └── usedoctest.py
│   │   │   │   ├── includes/
│   │   │   │   │   └── __init__.pxd
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── c14n.pxd
│   │   │   │   │   └── config.pxd
│   │   │   │   │   └── dtdvalid.pxd
│   │   │   │   │   └── etree_defs.h
│   │   │   │   │   └── etreepublic.pxd
│   │   │   │   │   ├── extlibs/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── zconf.h
│   │   │   │   │   │   └── zlib.h
│   │   │   │   │   └── htmlparser.pxd
│   │   │   │   │   ├── libexslt/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── exslt.h
│   │   │   │   │   │   └── exsltconfig.h
│   │   │   │   │   │   └── exsltexports.h
│   │   │   │   │   │   └── libexslt.h
│   │   │   │   │   ├── libxml/
│   │   │   │   │   │   └── HTMLparser.h
│   │   │   │   │   │   └── HTMLtree.h
│   │   │   │   │   │   └── SAX.h
│   │   │   │   │   │   └── SAX2.h
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── c14n.h
│   │   │   │   │   │   └── catalog.h
│   │   │   │   │   │   └── chvalid.h
│   │   │   │   │   │   └── debugXML.h
│   │   │   │   │   │   └── dict.h
│   │   │   │   │   │   └── encoding.h
│   │   │   │   │   │   └── entities.h
│   │   │   │   │   │   └── globals.h
│   │   │   │   │   │   └── hash.h
│   │   │   │   │   │   └── list.h
│   │   │   │   │   │   └── nanoftp.h
│   │   │   │   │   │   └── nanohttp.h
│   │   │   │   │   │   └── parser.h
│   │   │   │   │   │   └── parserInternals.h
│   │   │   │   │   │   └── pattern.h
│   │   │   │   │   │   └── relaxng.h
│   │   │   │   │   │   └── schemasInternals.h
│   │   │   │   │   │   └── schematron.h
│   │   │   │   │   │   └── threads.h
│   │   │   │   │   │   └── tree.h
│   │   │   │   │   │   └── uri.h
│   │   │   │   │   │   └── valid.h
│   │   │   │   │   │   └── xinclude.h
│   │   │   │   │   │   └── xlink.h
│   │   │   │   │   │   └── xmlIO.h
│   │   │   │   │   │   └── xmlautomata.h
│   │   │   │   │   │   └── xmlerror.h
│   │   │   │   │   │   └── xmlexports.h
│   │   │   │   │   │   └── xmlmemory.h
│   │   │   │   │   │   └── xmlmodule.h
│   │   │   │   │   │   └── xmlreader.h
│   │   │   │   │   │   └── xmlregexp.h
│   │   │   │   │   │   └── xmlsave.h
│   │   │   │   │   │   └── xmlschemas.h
│   │   │   │   │   │   └── xmlschemastypes.h
│   │   │   │   │   │   └── xmlstring.h
│   │   │   │   │   │   └── xmlunicode.h
│   │   │   │   │   │   └── xmlversion.h
│   │   │   │   │   │   └── xmlwriter.h
│   │   │   │   │   │   └── xpath.h
│   │   │   │   │   │   └── xpathInternals.h
│   │   │   │   │   │   └── xpointer.h
│   │   │   │   │   ├── libxslt/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── attributes.h
│   │   │   │   │   │   └── documents.h
│   │   │   │   │   │   └── extensions.h
│   │   │   │   │   │   └── extra.h
│   │   │   │   │   │   └── functions.h
│   │   │   │   │   │   └── imports.h
│   │   │   │   │   │   └── keys.h
│   │   │   │   │   │   └── libxslt.h
│   │   │   │   │   │   └── namespaces.h
│   │   │   │   │   │   └── numbersInternals.h
│   │   │   │   │   │   └── preproc.h
│   │   │   │   │   │   └── security.h
│   │   │   │   │   │   └── templates.h
│   │   │   │   │   │   └── transform.h
│   │   │   │   │   │   └── trio.h
│   │   │   │   │   │   └── triodef.h
│   │   │   │   │   │   └── variables.h
│   │   │   │   │   │   └── win32config.h
│   │   │   │   │   │   └── xslt.h
│   │   │   │   │   │   └── xsltInternals.h
│   │   │   │   │   │   └── xsltconfig.h
│   │   │   │   │   │   └── xsltexports.h
│   │   │   │   │   │   └── xsltlocale.h
│   │   │   │   │   │   └── xsltutils.h
│   │   │   │   │   └── lxml-version.h
│   │   │   │   │   └── relaxng.pxd
│   │   │   │   │   └── schematron.pxd
│   │   │   │   │   └── tree.pxd
│   │   │   │   │   └── uri.pxd
│   │   │   │   │   └── xinclude.pxd
│   │   │   │   │   └── xmlerror.pxd
│   │   │   │   │   └── xmlparser.pxd
│   │   │   │   │   └── xmlschema.pxd
│   │   │   │   │   └── xpath.pxd
│   │   │   │   │   └── xslt.pxd
│   │   │   │   ├── isoschematron/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   ├── resources/
│   │   │   │   │   │   ├── rng/
│   │   │   │   │   │   │   └── iso-schematron.rng
│   │   │   │   │   │   ├── xsl/
│   │   │   │   │   │   │   └── RNG2Schtrn.xsl
│   │   │   │   │   │   │   └── XSD2Schtrn.xsl
│   │   │   │   │   │   │   ├── iso-schematron-xslt1/
│   │   │   │   │   │   │   │   └── iso_abstract_expand.xsl
│   │   │   │   │   │   │   │   └── iso_dsdl_include.xsl
│   │   │   │   │   │   │   │   └── iso_schematron_message.xsl
│   │   │   │   │   │   │   │   └── iso_schematron_skeleton_for_xslt1.xsl
│   │   │   │   │   │   │   │   └── iso_svrl_for_xslt1.xsl
│   │   │   │   │   │   │   │   └── readme.txt
│   │   │   │   └── iterparse.pxi
│   │   │   │   └── lxml.etree.h
│   │   │   │   └── lxml.etree_api.h
│   │   │   │   └── nsclasses.pxi
│   │   │   │   └── objectify.cp313-win_amd64.pyd
│   │   │   │   └── objectify.pyx
│   │   │   │   └── objectpath.pxi
│   │   │   │   └── parser.pxi
│   │   │   │   └── parsertarget.pxi
│   │   │   │   └── proxy.pxi
│   │   │   │   └── public-api.pxi
│   │   │   │   └── pyclasslookup.py
│   │   │   │   └── readonlytree.pxi
│   │   │   │   └── relaxng.pxi
│   │   │   │   └── sax.cp313-win_amd64.pyd
│   │   │   │   └── sax.py
│   │   │   │   └── saxparser.pxi
│   │   │   │   └── schematron.pxi
│   │   │   │   └── serializer.pxi
│   │   │   │   └── usedoctest.py
│   │   │   │   └── xinclude.pxi
│   │   │   │   └── xmlerror.pxi
│   │   │   │   └── xmlid.pxi
│   │   │   │   └── xmlschema.pxi
│   │   │   │   └── xpath.pxi
│   │   │   │   └── xslt.pxi
│   │   │   │   └── xsltext.pxi
│   │   │   ├── lxml-5.3.1.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── LICENSES.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── markupsafe/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _native.cpython-313.pyc
│   │   │   │   └── _native.py
│   │   │   │   └── _speedups.c
│   │   │   │   └── _speedups.cp313-win_amd64.pyd
│   │   │   │   └── _speedups.pyi
│   │   │   │   └── py.typed
│   │   │   ├── numpy/
│   │   │   │   └── __config__.py
│   │   │   │   └── __config__.pyi
│   │   │   │   └── __init__.cython-30.pxd
│   │   │   │   └── __init__.pxd
│   │   │   │   └── __init__.py
│   │   │   │   └── __init__.pyi
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __config__.cpython-313.pyc
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _array_api_info.cpython-313.pyc
│   │   │   │   │   └── _configtool.cpython-313.pyc
│   │   │   │   │   └── _distributor_init.cpython-313.pyc
│   │   │   │   │   └── _expired_attrs_2_0.cpython-313.pyc
│   │   │   │   │   └── _globals.cpython-313.pyc
│   │   │   │   │   └── _pytesttester.cpython-313.pyc
│   │   │   │   │   └── conftest.cpython-313.pyc
│   │   │   │   │   └── ctypeslib.cpython-313.pyc
│   │   │   │   │   └── dtypes.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── matlib.cpython-313.pyc
│   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   └── _array_api_info.py
│   │   │   │   └── _array_api_info.pyi
│   │   │   │   └── _configtool.py
│   │   │   │   └── _configtool.pyi
│   │   │   │   ├── _core/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _add_newdocs.cpython-313.pyc
│   │   │   │   │   │   └── _add_newdocs_scalars.cpython-313.pyc
│   │   │   │   │   │   └── _asarray.cpython-313.pyc
│   │   │   │   │   │   └── _dtype.cpython-313.pyc
│   │   │   │   │   │   └── _dtype_ctypes.cpython-313.pyc
│   │   │   │   │   │   └── _exceptions.cpython-313.pyc
│   │   │   │   │   │   └── _internal.cpython-313.pyc
│   │   │   │   │   │   └── _machar.cpython-313.pyc
│   │   │   │   │   │   └── _methods.cpython-313.pyc
│   │   │   │   │   │   └── _string_helpers.cpython-313.pyc
│   │   │   │   │   │   └── _type_aliases.cpython-313.pyc
│   │   │   │   │   │   └── _ufunc_config.cpython-313.pyc
│   │   │   │   │   │   └── arrayprint.cpython-313.pyc
│   │   │   │   │   │   └── cversions.cpython-313.pyc
│   │   │   │   │   │   └── defchararray.cpython-313.pyc
│   │   │   │   │   │   └── einsumfunc.cpython-313.pyc
│   │   │   │   │   │   └── fromnumeric.cpython-313.pyc
│   │   │   │   │   │   └── function_base.cpython-313.pyc
│   │   │   │   │   │   └── getlimits.cpython-313.pyc
│   │   │   │   │   │   └── memmap.cpython-313.pyc
│   │   │   │   │   │   └── multiarray.cpython-313.pyc
│   │   │   │   │   │   └── numeric.cpython-313.pyc
│   │   │   │   │   │   └── numerictypes.cpython-313.pyc
│   │   │   │   │   │   └── overrides.cpython-313.pyc
│   │   │   │   │   │   └── printoptions.cpython-313.pyc
│   │   │   │   │   │   └── records.cpython-313.pyc
│   │   │   │   │   │   └── shape_base.cpython-313.pyc
│   │   │   │   │   │   └── strings.cpython-313.pyc
│   │   │   │   │   │   └── umath.cpython-313.pyc
│   │   │   │   │   └── _add_newdocs.py
│   │   │   │   │   └── _add_newdocs.pyi
│   │   │   │   │   └── _add_newdocs_scalars.py
│   │   │   │   │   └── _add_newdocs_scalars.pyi
│   │   │   │   │   └── _asarray.py
│   │   │   │   │   └── _asarray.pyi
│   │   │   │   │   └── _dtype.py
│   │   │   │   │   └── _dtype.pyi
│   │   │   │   │   └── _dtype_ctypes.py
│   │   │   │   │   └── _dtype_ctypes.pyi
│   │   │   │   │   └── _exceptions.py
│   │   │   │   │   └── _exceptions.pyi
│   │   │   │   │   └── _internal.py
│   │   │   │   │   └── _internal.pyi
│   │   │   │   │   └── _machar.py
│   │   │   │   │   └── _machar.pyi
│   │   │   │   │   └── _methods.py
│   │   │   │   │   └── _methods.pyi
│   │   │   │   │   └── _multiarray_tests.cp313-win_amd64.lib
│   │   │   │   │   └── _multiarray_tests.cp313-win_amd64.pyd
│   │   │   │   │   └── _multiarray_umath.cp313-win_amd64.lib
│   │   │   │   │   └── _multiarray_umath.cp313-win_amd64.pyd
│   │   │   │   │   └── _operand_flag_tests.cp313-win_amd64.lib
│   │   │   │   │   └── _operand_flag_tests.cp313-win_amd64.pyd
│   │   │   │   │   └── _rational_tests.cp313-win_amd64.lib
│   │   │   │   │   └── _rational_tests.cp313-win_amd64.pyd
│   │   │   │   │   └── _simd.cp313-win_amd64.lib
│   │   │   │   │   └── _simd.cp313-win_amd64.pyd
│   │   │   │   │   └── _simd.pyi
│   │   │   │   │   └── _string_helpers.py
│   │   │   │   │   └── _string_helpers.pyi
│   │   │   │   │   └── _struct_ufunc_tests.cp313-win_amd64.lib
│   │   │   │   │   └── _struct_ufunc_tests.cp313-win_amd64.pyd
│   │   │   │   │   └── _type_aliases.py
│   │   │   │   │   └── _type_aliases.pyi
│   │   │   │   │   └── _ufunc_config.py
│   │   │   │   │   └── _ufunc_config.pyi
│   │   │   │   │   └── _umath_tests.cp313-win_amd64.lib
│   │   │   │   │   └── _umath_tests.cp313-win_amd64.pyd
│   │   │   │   │   └── arrayprint.py
│   │   │   │   │   └── arrayprint.pyi
│   │   │   │   │   └── cversions.py
│   │   │   │   │   └── defchararray.py
│   │   │   │   │   └── defchararray.pyi
│   │   │   │   │   └── einsumfunc.py
│   │   │   │   │   └── einsumfunc.pyi
│   │   │   │   │   └── fromnumeric.py
│   │   │   │   │   └── fromnumeric.pyi
│   │   │   │   │   └── function_base.py
│   │   │   │   │   └── function_base.pyi
│   │   │   │   │   └── getlimits.py
│   │   │   │   │   └── getlimits.pyi
│   │   │   │   │   ├── include/
│   │   │   │   │   │   ├── numpy/
│   │   │   │   │   │   │   └── __multiarray_api.c
│   │   │   │   │   │   │   └── __multiarray_api.h
│   │   │   │   │   │   │   └── __ufunc_api.c
│   │   │   │   │   │   │   └── __ufunc_api.h
│   │   │   │   │   │   │   └── _neighborhood_iterator_imp.h
│   │   │   │   │   │   │   └── _numpyconfig.h
│   │   │   │   │   │   │   └── _public_dtype_api_table.h
│   │   │   │   │   │   │   └── arrayobject.h
│   │   │   │   │   │   │   └── arrayscalars.h
│   │   │   │   │   │   │   └── dtype_api.h
│   │   │   │   │   │   │   └── halffloat.h
│   │   │   │   │   │   │   └── ndarrayobject.h
│   │   │   │   │   │   │   └── ndarraytypes.h
│   │   │   │   │   │   │   └── npy_1_7_deprecated_api.h
│   │   │   │   │   │   │   └── npy_2_compat.h
│   │   │   │   │   │   │   └── npy_2_complexcompat.h
│   │   │   │   │   │   │   └── npy_3kcompat.h
│   │   │   │   │   │   │   └── npy_common.h
│   │   │   │   │   │   │   └── npy_cpu.h
│   │   │   │   │   │   │   └── npy_endian.h
│   │   │   │   │   │   │   └── npy_math.h
│   │   │   │   │   │   │   └── npy_no_deprecated_api.h
│   │   │   │   │   │   │   └── npy_os.h
│   │   │   │   │   │   │   └── numpyconfig.h
│   │   │   │   │   │   │   ├── random/
│   │   │   │   │   │   │   │   └── LICENSE.txt
│   │   │   │   │   │   │   │   └── bitgen.h
│   │   │   │   │   │   │   │   └── distributions.h
│   │   │   │   │   │   │   │   └── libdivide.h
│   │   │   │   │   │   │   └── ufuncobject.h
│   │   │   │   │   │   │   └── utils.h
│   │   │   │   │   ├── lib/
│   │   │   │   │   │   ├── npy-pkg-config/
│   │   │   │   │   │   │   └── mlib.ini
│   │   │   │   │   │   │   └── npymath.ini
│   │   │   │   │   │   └── npymath.lib
│   │   │   │   │   │   ├── pkgconfig/
│   │   │   │   │   │   │   └── numpy.pc
│   │   │   │   │   └── memmap.py
│   │   │   │   │   └── memmap.pyi
│   │   │   │   │   └── multiarray.py
│   │   │   │   │   └── multiarray.pyi
│   │   │   │   │   └── numeric.py
│   │   │   │   │   └── numeric.pyi
│   │   │   │   │   └── numerictypes.py
│   │   │   │   │   └── numerictypes.pyi
│   │   │   │   │   └── overrides.py
│   │   │   │   │   └── overrides.pyi
│   │   │   │   │   └── printoptions.py
│   │   │   │   │   └── printoptions.pyi
│   │   │   │   │   └── records.py
│   │   │   │   │   └── records.pyi
│   │   │   │   │   └── shape_base.py
│   │   │   │   │   └── shape_base.pyi
│   │   │   │   │   └── strings.py
│   │   │   │   │   └── strings.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── _locales.cpython-313.pyc
│   │   │   │   │   │   │   └── _natype.cpython-313.pyc
│   │   │   │   │   │   │   └── test__exceptions.cpython-313.pyc
│   │   │   │   │   │   │   └── test_abc.cpython-313.pyc
│   │   │   │   │   │   │   └── test_api.cpython-313.pyc
│   │   │   │   │   │   │   └── test_argparse.cpython-313.pyc
│   │   │   │   │   │   │   └── test_array_api_info.cpython-313.pyc
│   │   │   │   │   │   │   └── test_array_coercion.cpython-313.pyc
│   │   │   │   │   │   │   └── test_array_interface.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arraymethod.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arrayobject.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arrayprint.cpython-313.pyc
│   │   │   │   │   │   │   └── test_casting_floatingpoint_errors.cpython-313.pyc
│   │   │   │   │   │   │   └── test_casting_unittests.cpython-313.pyc
│   │   │   │   │   │   │   └── test_conversion_utils.cpython-313.pyc
│   │   │   │   │   │   │   └── test_cpu_dispatcher.cpython-313.pyc
│   │   │   │   │   │   │   └── test_cpu_features.cpython-313.pyc
│   │   │   │   │   │   │   └── test_custom_dtypes.cpython-313.pyc
│   │   │   │   │   │   │   └── test_cython.cpython-313.pyc
│   │   │   │   │   │   │   └── test_datetime.cpython-313.pyc
│   │   │   │   │   │   │   └── test_defchararray.cpython-313.pyc
│   │   │   │   │   │   │   └── test_deprecations.cpython-313.pyc
│   │   │   │   │   │   │   └── test_dlpack.cpython-313.pyc
│   │   │   │   │   │   │   └── test_dtype.cpython-313.pyc
│   │   │   │   │   │   │   └── test_einsum.cpython-313.pyc
│   │   │   │   │   │   │   └── test_errstate.cpython-313.pyc
│   │   │   │   │   │   │   └── test_extint128.cpython-313.pyc
│   │   │   │   │   │   │   └── test_function_base.cpython-313.pyc
│   │   │   │   │   │   │   └── test_getlimits.cpython-313.pyc
│   │   │   │   │   │   │   └── test_half.cpython-313.pyc
│   │   │   │   │   │   │   └── test_hashtable.cpython-313.pyc
│   │   │   │   │   │   │   └── test_indexerrors.cpython-313.pyc
│   │   │   │   │   │   │   └── test_indexing.cpython-313.pyc
│   │   │   │   │   │   │   └── test_item_selection.cpython-313.pyc
│   │   │   │   │   │   │   └── test_limited_api.cpython-313.pyc
│   │   │   │   │   │   │   └── test_longdouble.cpython-313.pyc
│   │   │   │   │   │   │   └── test_machar.cpython-313.pyc
│   │   │   │   │   │   │   └── test_mem_overlap.cpython-313.pyc
│   │   │   │   │   │   │   └── test_mem_policy.cpython-313.pyc
│   │   │   │   │   │   │   └── test_memmap.cpython-313.pyc
│   │   │   │   │   │   │   └── test_multiarray.cpython-313.pyc
│   │   │   │   │   │   │   └── test_multithreading.cpython-313.pyc
│   │   │   │   │   │   │   └── test_nditer.cpython-313.pyc
│   │   │   │   │   │   │   └── test_nep50_promotions.cpython-313.pyc
│   │   │   │   │   │   │   └── test_numeric.cpython-313.pyc
│   │   │   │   │   │   │   └── test_numerictypes.cpython-313.pyc
│   │   │   │   │   │   │   └── test_overrides.cpython-313.pyc
│   │   │   │   │   │   │   └── test_print.cpython-313.pyc
│   │   │   │   │   │   │   └── test_protocols.cpython-313.pyc
│   │   │   │   │   │   │   └── test_records.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   │   └── test_scalar_ctors.cpython-313.pyc
│   │   │   │   │   │   │   └── test_scalar_methods.cpython-313.pyc
│   │   │   │   │   │   │   └── test_scalarbuffer.cpython-313.pyc
│   │   │   │   │   │   │   └── test_scalarinherit.cpython-313.pyc
│   │   │   │   │   │   │   └── test_scalarmath.cpython-313.pyc
│   │   │   │   │   │   │   └── test_scalarprint.cpython-313.pyc
│   │   │   │   │   │   │   └── test_shape_base.cpython-313.pyc
│   │   │   │   │   │   │   └── test_simd.cpython-313.pyc
│   │   │   │   │   │   │   └── test_simd_module.cpython-313.pyc
│   │   │   │   │   │   │   └── test_stringdtype.cpython-313.pyc
│   │   │   │   │   │   │   └── test_strings.cpython-313.pyc
│   │   │   │   │   │   │   └── test_ufunc.cpython-313.pyc
│   │   │   │   │   │   │   └── test_umath.cpython-313.pyc
│   │   │   │   │   │   │   └── test_umath_accuracy.cpython-313.pyc
│   │   │   │   │   │   │   └── test_umath_complex.cpython-313.pyc
│   │   │   │   │   │   │   └── test_unicode.cpython-313.pyc
│   │   │   │   │   │   └── _locales.py
│   │   │   │   │   │   └── _natype.py
│   │   │   │   │   │   ├── data/
│   │   │   │   │   │   │   └── astype_copy.pkl
│   │   │   │   │   │   │   └── generate_umath_validation_data.cpp
│   │   │   │   │   │   │   └── recarray_from_file.fits
│   │   │   │   │   │   │   └── umath-validation-set-README.txt
│   │   │   │   │   │   │   └── umath-validation-set-arccos.csv
│   │   │   │   │   │   │   └── umath-validation-set-arccosh.csv
│   │   │   │   │   │   │   └── umath-validation-set-arcsin.csv
│   │   │   │   │   │   │   └── umath-validation-set-arcsinh.csv
│   │   │   │   │   │   │   └── umath-validation-set-arctan.csv
│   │   │   │   │   │   │   └── umath-validation-set-arctanh.csv
│   │   │   │   │   │   │   └── umath-validation-set-cbrt.csv
│   │   │   │   │   │   │   └── umath-validation-set-cos.csv
│   │   │   │   │   │   │   └── umath-validation-set-cosh.csv
│   │   │   │   │   │   │   └── umath-validation-set-exp.csv
│   │   │   │   │   │   │   └── umath-validation-set-exp2.csv
│   │   │   │   │   │   │   └── umath-validation-set-expm1.csv
│   │   │   │   │   │   │   └── umath-validation-set-log.csv
│   │   │   │   │   │   │   └── umath-validation-set-log10.csv
│   │   │   │   │   │   │   └── umath-validation-set-log1p.csv
│   │   │   │   │   │   │   └── umath-validation-set-log2.csv
│   │   │   │   │   │   │   └── umath-validation-set-sin.csv
│   │   │   │   │   │   │   └── umath-validation-set-sinh.csv
│   │   │   │   │   │   │   └── umath-validation-set-tan.csv
│   │   │   │   │   │   │   └── umath-validation-set-tanh.csv
│   │   │   │   │   │   ├── examples/
│   │   │   │   │   │   │   ├── cython/
│   │   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   │   └── setup.cpython-313.pyc
│   │   │   │   │   │   │   │   └── checks.pyx
│   │   │   │   │   │   │   │   └── meson.build
│   │   │   │   │   │   │   │   └── setup.py
│   │   │   │   │   │   │   ├── limited_api/
│   │   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   │   └── setup.cpython-313.pyc
│   │   │   │   │   │   │   │   └── limited_api1.c
│   │   │   │   │   │   │   │   └── limited_api2.pyx
│   │   │   │   │   │   │   │   └── limited_api_latest.c
│   │   │   │   │   │   │   │   └── meson.build
│   │   │   │   │   │   │   │   └── setup.py
│   │   │   │   │   │   └── test__exceptions.py
│   │   │   │   │   │   └── test_abc.py
│   │   │   │   │   │   └── test_api.py
│   │   │   │   │   │   └── test_argparse.py
│   │   │   │   │   │   └── test_array_api_info.py
│   │   │   │   │   │   └── test_array_coercion.py
│   │   │   │   │   │   └── test_array_interface.py
│   │   │   │   │   │   └── test_arraymethod.py
│   │   │   │   │   │   └── test_arrayobject.py
│   │   │   │   │   │   └── test_arrayprint.py
│   │   │   │   │   │   └── test_casting_floatingpoint_errors.py
│   │   │   │   │   │   └── test_casting_unittests.py
│   │   │   │   │   │   └── test_conversion_utils.py
│   │   │   │   │   │   └── test_cpu_dispatcher.py
│   │   │   │   │   │   └── test_cpu_features.py
│   │   │   │   │   │   └── test_custom_dtypes.py
│   │   │   │   │   │   └── test_cython.py
│   │   │   │   │   │   └── test_datetime.py
│   │   │   │   │   │   └── test_defchararray.py
│   │   │   │   │   │   └── test_deprecations.py
│   │   │   │   │   │   └── test_dlpack.py
│   │   │   │   │   │   └── test_dtype.py
│   │   │   │   │   │   └── test_einsum.py
│   │   │   │   │   │   └── test_errstate.py
│   │   │   │   │   │   └── test_extint128.py
│   │   │   │   │   │   └── test_function_base.py
│   │   │   │   │   │   └── test_getlimits.py
│   │   │   │   │   │   └── test_half.py
│   │   │   │   │   │   └── test_hashtable.py
│   │   │   │   │   │   └── test_indexerrors.py
│   │   │   │   │   │   └── test_indexing.py
│   │   │   │   │   │   └── test_item_selection.py
│   │   │   │   │   │   └── test_limited_api.py
│   │   │   │   │   │   └── test_longdouble.py
│   │   │   │   │   │   └── test_machar.py
│   │   │   │   │   │   └── test_mem_overlap.py
│   │   │   │   │   │   └── test_mem_policy.py
│   │   │   │   │   │   └── test_memmap.py
│   │   │   │   │   │   └── test_multiarray.py
│   │   │   │   │   │   └── test_multithreading.py
│   │   │   │   │   │   └── test_nditer.py
│   │   │   │   │   │   └── test_nep50_promotions.py
│   │   │   │   │   │   └── test_numeric.py
│   │   │   │   │   │   └── test_numerictypes.py
│   │   │   │   │   │   └── test_overrides.py
│   │   │   │   │   │   └── test_print.py
│   │   │   │   │   │   └── test_protocols.py
│   │   │   │   │   │   └── test_records.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   │   │   └── test_scalar_ctors.py
│   │   │   │   │   │   └── test_scalar_methods.py
│   │   │   │   │   │   └── test_scalarbuffer.py
│   │   │   │   │   │   └── test_scalarinherit.py
│   │   │   │   │   │   └── test_scalarmath.py
│   │   │   │   │   │   └── test_scalarprint.py
│   │   │   │   │   │   └── test_shape_base.py
│   │   │   │   │   │   └── test_simd.py
│   │   │   │   │   │   └── test_simd_module.py
│   │   │   │   │   │   └── test_stringdtype.py
│   │   │   │   │   │   └── test_strings.py
│   │   │   │   │   │   └── test_ufunc.py
│   │   │   │   │   │   └── test_umath.py
│   │   │   │   │   │   └── test_umath_accuracy.py
│   │   │   │   │   │   └── test_umath_complex.py
│   │   │   │   │   │   └── test_unicode.py
│   │   │   │   │   └── umath.py
│   │   │   │   │   └── umath.pyi
│   │   │   │   └── _distributor_init.py
│   │   │   │   └── _distributor_init.pyi
│   │   │   │   └── _expired_attrs_2_0.py
│   │   │   │   └── _expired_attrs_2_0.pyi
│   │   │   │   └── _globals.py
│   │   │   │   └── _globals.pyi
│   │   │   │   ├── _pyinstaller/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── hook-numpy.cpython-313.pyc
│   │   │   │   │   └── hook-numpy.py
│   │   │   │   │   └── hook-numpy.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── pyinstaller-smoke.cpython-313.pyc
│   │   │   │   │   │   │   └── test_pyinstaller.cpython-313.pyc
│   │   │   │   │   │   └── pyinstaller-smoke.py
│   │   │   │   │   │   └── test_pyinstaller.py
│   │   │   │   └── _pytesttester.py
│   │   │   │   └── _pytesttester.pyi
│   │   │   │   ├── _typing/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _add_docstring.cpython-313.pyc
│   │   │   │   │   │   └── _array_like.cpython-313.pyc
│   │   │   │   │   │   └── _char_codes.cpython-313.pyc
│   │   │   │   │   │   └── _dtype_like.cpython-313.pyc
│   │   │   │   │   │   └── _extended_precision.cpython-313.pyc
│   │   │   │   │   │   └── _nbit.cpython-313.pyc
│   │   │   │   │   │   └── _nbit_base.cpython-313.pyc
│   │   │   │   │   │   └── _nested_sequence.cpython-313.pyc
│   │   │   │   │   │   └── _scalars.cpython-313.pyc
│   │   │   │   │   │   └── _shape.cpython-313.pyc
│   │   │   │   │   │   └── _ufunc.cpython-313.pyc
│   │   │   │   │   └── _add_docstring.py
│   │   │   │   │   └── _array_like.py
│   │   │   │   │   └── _callable.pyi
│   │   │   │   │   └── _char_codes.py
│   │   │   │   │   └── _dtype_like.py
│   │   │   │   │   └── _extended_precision.py
│   │   │   │   │   └── _nbit.py
│   │   │   │   │   └── _nbit_base.py
│   │   │   │   │   └── _nested_sequence.py
│   │   │   │   │   └── _scalars.py
│   │   │   │   │   └── _shape.py
│   │   │   │   │   └── _ufunc.py
│   │   │   │   │   └── _ufunc.pyi
│   │   │   │   ├── _utils/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _convertions.cpython-313.pyc
│   │   │   │   │   │   └── _inspect.cpython-313.pyc
│   │   │   │   │   │   └── _pep440.cpython-313.pyc
│   │   │   │   │   └── _convertions.py
│   │   │   │   │   └── _convertions.pyi
│   │   │   │   │   └── _inspect.py
│   │   │   │   │   └── _inspect.pyi
│   │   │   │   │   └── _pep440.py
│   │   │   │   │   └── _pep440.pyi
│   │   │   │   ├── char/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   ├── compat/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── py3k.cpython-313.pyc
│   │   │   │   │   └── py3k.py
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   └── conftest.py
│   │   │   │   ├── core/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _dtype.cpython-313.pyc
│   │   │   │   │   │   └── _dtype_ctypes.cpython-313.pyc
│   │   │   │   │   │   └── _internal.cpython-313.pyc
│   │   │   │   │   │   └── _multiarray_umath.cpython-313.pyc
│   │   │   │   │   │   └── _utils.cpython-313.pyc
│   │   │   │   │   │   └── arrayprint.cpython-313.pyc
│   │   │   │   │   │   └── defchararray.cpython-313.pyc
│   │   │   │   │   │   └── einsumfunc.cpython-313.pyc
│   │   │   │   │   │   └── fromnumeric.cpython-313.pyc
│   │   │   │   │   │   └── function_base.cpython-313.pyc
│   │   │   │   │   │   └── getlimits.cpython-313.pyc
│   │   │   │   │   │   └── multiarray.cpython-313.pyc
│   │   │   │   │   │   └── numeric.cpython-313.pyc
│   │   │   │   │   │   └── numerictypes.cpython-313.pyc
│   │   │   │   │   │   └── overrides.cpython-313.pyc
│   │   │   │   │   │   └── records.cpython-313.pyc
│   │   │   │   │   │   └── shape_base.cpython-313.pyc
│   │   │   │   │   │   └── umath.cpython-313.pyc
│   │   │   │   │   └── _dtype.py
│   │   │   │   │   └── _dtype.pyi
│   │   │   │   │   └── _dtype_ctypes.py
│   │   │   │   │   └── _dtype_ctypes.pyi
│   │   │   │   │   └── _internal.py
│   │   │   │   │   └── _multiarray_umath.py
│   │   │   │   │   └── _utils.py
│   │   │   │   │   └── arrayprint.py
│   │   │   │   │   └── defchararray.py
│   │   │   │   │   └── einsumfunc.py
│   │   │   │   │   └── fromnumeric.py
│   │   │   │   │   └── function_base.py
│   │   │   │   │   └── getlimits.py
│   │   │   │   │   └── multiarray.py
│   │   │   │   │   └── numeric.py
│   │   │   │   │   └── numerictypes.py
│   │   │   │   │   └── overrides.py
│   │   │   │   │   └── overrides.pyi
│   │   │   │   │   └── records.py
│   │   │   │   │   └── shape_base.py
│   │   │   │   │   └── umath.py
│   │   │   │   └── ctypeslib.py
│   │   │   │   └── ctypeslib.pyi
│   │   │   │   ├── doc/
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── ufuncs.cpython-313.pyc
│   │   │   │   │   └── ufuncs.py
│   │   │   │   └── dtypes.py
│   │   │   │   └── dtypes.pyi
│   │   │   │   └── exceptions.py
│   │   │   │   └── exceptions.pyi
│   │   │   │   ├── f2py/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   └── __main__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   │   └── __version__.cpython-313.pyc
│   │   │   │   │   │   └── _isocbind.cpython-313.pyc
│   │   │   │   │   │   └── _src_pyf.cpython-313.pyc
│   │   │   │   │   │   └── auxfuncs.cpython-313.pyc
│   │   │   │   │   │   └── capi_maps.cpython-313.pyc
│   │   │   │   │   │   └── cb_rules.cpython-313.pyc
│   │   │   │   │   │   └── cfuncs.cpython-313.pyc
│   │   │   │   │   │   └── common_rules.cpython-313.pyc
│   │   │   │   │   │   └── crackfortran.cpython-313.pyc
│   │   │   │   │   │   └── diagnose.cpython-313.pyc
│   │   │   │   │   │   └── f2py2e.cpython-313.pyc
│   │   │   │   │   │   └── f90mod_rules.cpython-313.pyc
│   │   │   │   │   │   └── func2subr.cpython-313.pyc
│   │   │   │   │   │   └── rules.cpython-313.pyc
│   │   │   │   │   │   └── symbolic.cpython-313.pyc
│   │   │   │   │   │   └── use_rules.cpython-313.pyc
│   │   │   │   │   └── __version__.py
│   │   │   │   │   ├── _backends/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _backend.cpython-313.pyc
│   │   │   │   │   │   │   └── _distutils.cpython-313.pyc
│   │   │   │   │   │   │   └── _meson.cpython-313.pyc
│   │   │   │   │   │   └── _backend.py
│   │   │   │   │   │   └── _distutils.py
│   │   │   │   │   │   └── _meson.py
│   │   │   │   │   │   └── meson.build.template
│   │   │   │   │   └── _isocbind.py
│   │   │   │   │   └── _src_pyf.py
│   │   │   │   │   └── auxfuncs.py
│   │   │   │   │   └── capi_maps.py
│   │   │   │   │   └── cb_rules.py
│   │   │   │   │   └── cfuncs.py
│   │   │   │   │   └── common_rules.py
│   │   │   │   │   └── crackfortran.py
│   │   │   │   │   └── diagnose.py
│   │   │   │   │   └── f2py2e.py
│   │   │   │   │   └── f90mod_rules.py
│   │   │   │   │   └── func2subr.py
│   │   │   │   │   └── rules.py
│   │   │   │   │   └── setup.cfg
│   │   │   │   │   ├── src/
│   │   │   │   │   │   └── fortranobject.c
│   │   │   │   │   │   └── fortranobject.h
│   │   │   │   │   └── symbolic.py
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_abstract_interface.cpython-313.pyc
│   │   │   │   │   │   │   └── test_array_from_pyobj.cpython-313.pyc
│   │   │   │   │   │   │   └── test_assumed_shape.cpython-313.pyc
│   │   │   │   │   │   │   └── test_block_docstring.cpython-313.pyc
│   │   │   │   │   │   │   └── test_callback.cpython-313.pyc
│   │   │   │   │   │   │   └── test_character.cpython-313.pyc
│   │   │   │   │   │   │   └── test_common.cpython-313.pyc
│   │   │   │   │   │   │   └── test_crackfortran.cpython-313.pyc
│   │   │   │   │   │   │   └── test_data.cpython-313.pyc
│   │   │   │   │   │   │   └── test_docs.cpython-313.pyc
│   │   │   │   │   │   │   └── test_f2cmap.cpython-313.pyc
│   │   │   │   │   │   │   └── test_f2py2e.cpython-313.pyc
│   │   │   │   │   │   │   └── test_isoc.cpython-313.pyc
│   │   │   │   │   │   │   └── test_kind.cpython-313.pyc
│   │   │   │   │   │   │   └── test_mixed.cpython-313.pyc
│   │   │   │   │   │   │   └── test_modules.cpython-313.pyc
│   │   │   │   │   │   │   └── test_parameter.cpython-313.pyc
│   │   │   │   │   │   │   └── test_pyf_src.cpython-313.pyc
│   │   │   │   │   │   │   └── test_quoted_character.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   │   └── test_return_character.cpython-313.pyc
│   │   │   │   │   │   │   └── test_return_complex.cpython-313.pyc
│   │   │   │   │   │   │   └── test_return_integer.cpython-313.pyc
│   │   │   │   │   │   │   └── test_return_logical.cpython-313.pyc
│   │   │   │   │   │   │   └── test_return_real.cpython-313.pyc
│   │   │   │   │   │   │   └── test_routines.cpython-313.pyc
│   │   │   │   │   │   │   └── test_semicolon_split.cpython-313.pyc
│   │   │   │   │   │   │   └── test_size.cpython-313.pyc
│   │   │   │   │   │   │   └── test_string.cpython-313.pyc
│   │   │   │   │   │   │   └── test_symbolic.cpython-313.pyc
│   │   │   │   │   │   │   └── test_value_attrspec.cpython-313.pyc
│   │   │   │   │   │   │   └── util.cpython-313.pyc
│   │   │   │   │   │   ├── src/
│   │   │   │   │   │   │   ├── abstract_interface/
│   │   │   │   │   │   │   │   └── foo.f90
│   │   │   │   │   │   │   │   └── gh18403_mod.f90
│   │   │   │   │   │   │   ├── array_from_pyobj/
│   │   │   │   │   │   │   │   └── wrapmodule.c
│   │   │   │   │   │   │   ├── assumed_shape/
│   │   │   │   │   │   │   │   └── .f2py_f2cmap
│   │   │   │   │   │   │   │   └── foo_free.f90
│   │   │   │   │   │   │   │   └── foo_mod.f90
│   │   │   │   │   │   │   │   └── foo_use.f90
│   │   │   │   │   │   │   │   └── precision.f90
│   │   │   │   │   │   │   ├── block_docstring/
│   │   │   │   │   │   │   │   └── foo.f
│   │   │   │   │   │   │   ├── callback/
│   │   │   │   │   │   │   │   └── foo.f
│   │   │   │   │   │   │   │   └── gh17797.f90
│   │   │   │   │   │   │   │   └── gh18335.f90
│   │   │   │   │   │   │   │   └── gh25211.f
│   │   │   │   │   │   │   │   └── gh25211.pyf
│   │   │   │   │   │   │   │   └── gh26681.f90
│   │   │   │   │   │   │   ├── cli/
│   │   │   │   │   │   │   │   └── gh_22819.pyf
│   │   │   │   │   │   │   │   └── hi77.f
│   │   │   │   │   │   │   │   └── hiworld.f90
│   │   │   │   │   │   │   ├── common/
│   │   │   │   │   │   │   │   └── block.f
│   │   │   │   │   │   │   │   └── gh19161.f90
│   │   │   │   │   │   │   ├── crackfortran/
│   │   │   │   │   │   │   │   └── accesstype.f90
│   │   │   │   │   │   │   │   └── data_common.f
│   │   │   │   │   │   │   │   └── data_multiplier.f
│   │   │   │   │   │   │   │   └── data_stmts.f90
│   │   │   │   │   │   │   │   └── data_with_comments.f
│   │   │   │   │   │   │   │   └── foo_deps.f90
│   │   │   │   │   │   │   │   └── gh15035.f
│   │   │   │   │   │   │   │   └── gh17859.f
│   │   │   │   │   │   │   │   └── gh22648.pyf
│   │   │   │   │   │   │   │   └── gh23533.f
│   │   │   │   │   │   │   │   └── gh23598.f90
│   │   │   │   │   │   │   │   └── gh23598Warn.f90
│   │   │   │   │   │   │   │   └── gh23879.f90
│   │   │   │   │   │   │   │   └── gh27697.f90
│   │   │   │   │   │   │   │   └── gh2848.f90
│   │   │   │   │   │   │   │   └── operators.f90
│   │   │   │   │   │   │   │   └── privatemod.f90
│   │   │   │   │   │   │   │   └── publicmod.f90
│   │   │   │   │   │   │   │   └── pubprivmod.f90
│   │   │   │   │   │   │   │   └── unicode_comment.f90
│   │   │   │   │   │   │   ├── f2cmap/
│   │   │   │   │   │   │   │   └── .f2py_f2cmap
│   │   │   │   │   │   │   │   └── isoFortranEnvMap.f90
│   │   │   │   │   │   │   ├── isocintrin/
│   │   │   │   │   │   │   │   └── isoCtests.f90
│   │   │   │   │   │   │   ├── kind/
│   │   │   │   │   │   │   │   └── foo.f90
│   │   │   │   │   │   │   ├── mixed/
│   │   │   │   │   │   │   │   └── foo.f
│   │   │   │   │   │   │   │   └── foo_fixed.f90
│   │   │   │   │   │   │   │   └── foo_free.f90
│   │   │   │   │   │   │   ├── modules/
│   │   │   │   │   │   │   │   ├── gh25337/
│   │   │   │   │   │   │   │   │   └── data.f90
│   │   │   │   │   │   │   │   │   └── use_data.f90
│   │   │   │   │   │   │   │   ├── gh26920/
│   │   │   │   │   │   │   │   │   └── two_mods_with_no_public_entities.f90
│   │   │   │   │   │   │   │   │   └── two_mods_with_one_public_routine.f90
│   │   │   │   │   │   │   │   └── module_data_docstring.f90
│   │   │   │   │   │   │   │   └── use_modules.f90
│   │   │   │   │   │   │   ├── negative_bounds/
│   │   │   │   │   │   │   │   └── issue_20853.f90
│   │   │   │   │   │   │   ├── parameter/
│   │   │   │   │   │   │   │   └── constant_array.f90
│   │   │   │   │   │   │   │   └── constant_both.f90
│   │   │   │   │   │   │   │   └── constant_compound.f90
│   │   │   │   │   │   │   │   └── constant_integer.f90
│   │   │   │   │   │   │   │   └── constant_non_compound.f90
│   │   │   │   │   │   │   │   └── constant_real.f90
│   │   │   │   │   │   │   ├── quoted_character/
│   │   │   │   │   │   │   │   └── foo.f
│   │   │   │   │   │   │   ├── regression/
│   │   │   │   │   │   │   │   └── AB.inc
│   │   │   │   │   │   │   │   └── assignOnlyModule.f90
│   │   │   │   │   │   │   │   └── datonly.f90
│   │   │   │   │   │   │   │   └── f77comments.f
│   │   │   │   │   │   │   │   └── f77fixedform.f95
│   │   │   │   │   │   │   │   └── f90continuation.f90
│   │   │   │   │   │   │   │   └── incfile.f90
│   │   │   │   │   │   │   │   └── inout.f90
│   │   │   │   │   │   │   │   └── lower_f2py_fortran.f90
│   │   │   │   │   │   │   ├── return_character/
│   │   │   │   │   │   │   │   └── foo77.f
│   │   │   │   │   │   │   │   └── foo90.f90
│   │   │   │   │   │   │   ├── return_complex/
│   │   │   │   │   │   │   │   └── foo77.f
│   │   │   │   │   │   │   │   └── foo90.f90
│   │   │   │   │   │   │   ├── return_integer/
│   │   │   │   │   │   │   │   └── foo77.f
│   │   │   │   │   │   │   │   └── foo90.f90
│   │   │   │   │   │   │   ├── return_logical/
│   │   │   │   │   │   │   │   └── foo77.f
│   │   │   │   │   │   │   │   └── foo90.f90
│   │   │   │   │   │   │   ├── return_real/
│   │   │   │   │   │   │   │   └── foo77.f
│   │   │   │   │   │   │   │   └── foo90.f90
│   │   │   │   │   │   │   ├── routines/
│   │   │   │   │   │   │   │   └── funcfortranname.f
│   │   │   │   │   │   │   │   └── funcfortranname.pyf
│   │   │   │   │   │   │   │   └── subrout.f
│   │   │   │   │   │   │   │   └── subrout.pyf
│   │   │   │   │   │   │   ├── size/
│   │   │   │   │   │   │   │   └── foo.f90
│   │   │   │   │   │   │   ├── string/
│   │   │   │   │   │   │   │   └── char.f90
│   │   │   │   │   │   │   │   └── fixed_string.f90
│   │   │   │   │   │   │   │   └── gh24008.f
│   │   │   │   │   │   │   │   └── gh24662.f90
│   │   │   │   │   │   │   │   └── gh25286.f90
│   │   │   │   │   │   │   │   └── gh25286.pyf
│   │   │   │   │   │   │   │   └── gh25286_bc.pyf
│   │   │   │   │   │   │   │   └── scalar_string.f90
│   │   │   │   │   │   │   │   └── string.f
│   │   │   │   │   │   │   ├── value_attrspec/
│   │   │   │   │   │   │   │   └── gh21665.f90
│   │   │   │   │   │   └── test_abstract_interface.py
│   │   │   │   │   │   └── test_array_from_pyobj.py
│   │   │   │   │   │   └── test_assumed_shape.py
│   │   │   │   │   │   └── test_block_docstring.py
│   │   │   │   │   │   └── test_callback.py
│   │   │   │   │   │   └── test_character.py
│   │   │   │   │   │   └── test_common.py
│   │   │   │   │   │   └── test_crackfortran.py
│   │   │   │   │   │   └── test_data.py
│   │   │   │   │   │   └── test_docs.py
│   │   │   │   │   │   └── test_f2cmap.py
│   │   │   │   │   │   └── test_f2py2e.py
│   │   │   │   │   │   └── test_isoc.py
│   │   │   │   │   │   └── test_kind.py
│   │   │   │   │   │   └── test_mixed.py
│   │   │   │   │   │   └── test_modules.py
│   │   │   │   │   │   └── test_parameter.py
│   │   │   │   │   │   └── test_pyf_src.py
│   │   │   │   │   │   └── test_quoted_character.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   │   │   └── test_return_character.py
│   │   │   │   │   │   └── test_return_complex.py
│   │   │   │   │   │   └── test_return_integer.py
│   │   │   │   │   │   └── test_return_logical.py
│   │   │   │   │   │   └── test_return_real.py
│   │   │   │   │   │   └── test_routines.py
│   │   │   │   │   │   └── test_semicolon_split.py
│   │   │   │   │   │   └── test_size.py
│   │   │   │   │   │   └── test_string.py
│   │   │   │   │   │   └── test_symbolic.py
│   │   │   │   │   │   └── test_value_attrspec.py
│   │   │   │   │   │   └── util.py
│   │   │   │   │   └── use_rules.py
│   │   │   │   ├── fft/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _helper.cpython-313.pyc
│   │   │   │   │   │   └── _pocketfft.cpython-313.pyc
│   │   │   │   │   │   └── helper.cpython-313.pyc
│   │   │   │   │   └── _helper.py
│   │   │   │   │   └── _helper.pyi
│   │   │   │   │   └── _pocketfft.py
│   │   │   │   │   └── _pocketfft.pyi
│   │   │   │   │   └── _pocketfft_umath.cp313-win_amd64.lib
│   │   │   │   │   └── _pocketfft_umath.cp313-win_amd64.pyd
│   │   │   │   │   └── helper.py
│   │   │   │   │   └── helper.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_helper.cpython-313.pyc
│   │   │   │   │   │   │   └── test_pocketfft.cpython-313.pyc
│   │   │   │   │   │   └── test_helper.py
│   │   │   │   │   │   └── test_pocketfft.py
│   │   │   │   ├── lib/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _array_utils_impl.cpython-313.pyc
│   │   │   │   │   │   └── _arraypad_impl.cpython-313.pyc
│   │   │   │   │   │   └── _arraysetops_impl.cpython-313.pyc
│   │   │   │   │   │   └── _arrayterator_impl.cpython-313.pyc
│   │   │   │   │   │   └── _datasource.cpython-313.pyc
│   │   │   │   │   │   └── _function_base_impl.cpython-313.pyc
│   │   │   │   │   │   └── _histograms_impl.cpython-313.pyc
│   │   │   │   │   │   └── _index_tricks_impl.cpython-313.pyc
│   │   │   │   │   │   └── _iotools.cpython-313.pyc
│   │   │   │   │   │   └── _nanfunctions_impl.cpython-313.pyc
│   │   │   │   │   │   └── _npyio_impl.cpython-313.pyc
│   │   │   │   │   │   └── _polynomial_impl.cpython-313.pyc
│   │   │   │   │   │   └── _scimath_impl.cpython-313.pyc
│   │   │   │   │   │   └── _shape_base_impl.cpython-313.pyc
│   │   │   │   │   │   └── _stride_tricks_impl.cpython-313.pyc
│   │   │   │   │   │   └── _twodim_base_impl.cpython-313.pyc
│   │   │   │   │   │   └── _type_check_impl.cpython-313.pyc
│   │   │   │   │   │   └── _ufunclike_impl.cpython-313.pyc
│   │   │   │   │   │   └── _user_array_impl.cpython-313.pyc
│   │   │   │   │   │   └── _utils_impl.cpython-313.pyc
│   │   │   │   │   │   └── _version.cpython-313.pyc
│   │   │   │   │   │   └── array_utils.cpython-313.pyc
│   │   │   │   │   │   └── format.cpython-313.pyc
│   │   │   │   │   │   └── introspect.cpython-313.pyc
│   │   │   │   │   │   └── mixins.cpython-313.pyc
│   │   │   │   │   │   └── npyio.cpython-313.pyc
│   │   │   │   │   │   └── recfunctions.cpython-313.pyc
│   │   │   │   │   │   └── scimath.cpython-313.pyc
│   │   │   │   │   │   └── stride_tricks.cpython-313.pyc
│   │   │   │   │   │   └── user_array.cpython-313.pyc
│   │   │   │   │   └── _array_utils_impl.py
│   │   │   │   │   └── _array_utils_impl.pyi
│   │   │   │   │   └── _arraypad_impl.py
│   │   │   │   │   └── _arraypad_impl.pyi
│   │   │   │   │   └── _arraysetops_impl.py
│   │   │   │   │   └── _arraysetops_impl.pyi
│   │   │   │   │   └── _arrayterator_impl.py
│   │   │   │   │   └── _arrayterator_impl.pyi
│   │   │   │   │   └── _datasource.py
│   │   │   │   │   └── _datasource.pyi
│   │   │   │   │   └── _function_base_impl.py
│   │   │   │   │   └── _function_base_impl.pyi
│   │   │   │   │   └── _histograms_impl.py
│   │   │   │   │   └── _histograms_impl.pyi
│   │   │   │   │   └── _index_tricks_impl.py
│   │   │   │   │   └── _index_tricks_impl.pyi
│   │   │   │   │   └── _iotools.py
│   │   │   │   │   └── _iotools.pyi
│   │   │   │   │   └── _nanfunctions_impl.py
│   │   │   │   │   └── _nanfunctions_impl.pyi
│   │   │   │   │   └── _npyio_impl.py
│   │   │   │   │   └── _npyio_impl.pyi
│   │   │   │   │   └── _polynomial_impl.py
│   │   │   │   │   └── _polynomial_impl.pyi
│   │   │   │   │   └── _scimath_impl.py
│   │   │   │   │   └── _scimath_impl.pyi
│   │   │   │   │   └── _shape_base_impl.py
│   │   │   │   │   └── _shape_base_impl.pyi
│   │   │   │   │   └── _stride_tricks_impl.py
│   │   │   │   │   └── _stride_tricks_impl.pyi
│   │   │   │   │   └── _twodim_base_impl.py
│   │   │   │   │   └── _twodim_base_impl.pyi
│   │   │   │   │   └── _type_check_impl.py
│   │   │   │   │   └── _type_check_impl.pyi
│   │   │   │   │   └── _ufunclike_impl.py
│   │   │   │   │   └── _ufunclike_impl.pyi
│   │   │   │   │   └── _user_array_impl.py
│   │   │   │   │   └── _user_array_impl.pyi
│   │   │   │   │   └── _utils_impl.py
│   │   │   │   │   └── _utils_impl.pyi
│   │   │   │   │   └── _version.py
│   │   │   │   │   └── _version.pyi
│   │   │   │   │   └── array_utils.py
│   │   │   │   │   └── array_utils.pyi
│   │   │   │   │   └── format.py
│   │   │   │   │   └── format.pyi
│   │   │   │   │   └── introspect.py
│   │   │   │   │   └── introspect.pyi
│   │   │   │   │   └── mixins.py
│   │   │   │   │   └── mixins.pyi
│   │   │   │   │   └── npyio.py
│   │   │   │   │   └── npyio.pyi
│   │   │   │   │   └── recfunctions.py
│   │   │   │   │   └── recfunctions.pyi
│   │   │   │   │   └── scimath.py
│   │   │   │   │   └── scimath.pyi
│   │   │   │   │   └── stride_tricks.py
│   │   │   │   │   └── stride_tricks.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test__datasource.cpython-313.pyc
│   │   │   │   │   │   │   └── test__iotools.cpython-313.pyc
│   │   │   │   │   │   │   └── test__version.cpython-313.pyc
│   │   │   │   │   │   │   └── test_array_utils.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arraypad.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arraysetops.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arrayterator.cpython-313.pyc
│   │   │   │   │   │   │   └── test_format.cpython-313.pyc
│   │   │   │   │   │   │   └── test_function_base.cpython-313.pyc
│   │   │   │   │   │   │   └── test_histograms.cpython-313.pyc
│   │   │   │   │   │   │   └── test_index_tricks.cpython-313.pyc
│   │   │   │   │   │   │   └── test_io.cpython-313.pyc
│   │   │   │   │   │   │   └── test_loadtxt.cpython-313.pyc
│   │   │   │   │   │   │   └── test_mixins.cpython-313.pyc
│   │   │   │   │   │   │   └── test_nanfunctions.cpython-313.pyc
│   │   │   │   │   │   │   └── test_packbits.cpython-313.pyc
│   │   │   │   │   │   │   └── test_polynomial.cpython-313.pyc
│   │   │   │   │   │   │   └── test_recfunctions.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   │   └── test_shape_base.cpython-313.pyc
│   │   │   │   │   │   │   └── test_stride_tricks.cpython-313.pyc
│   │   │   │   │   │   │   └── test_twodim_base.cpython-313.pyc
│   │   │   │   │   │   │   └── test_type_check.cpython-313.pyc
│   │   │   │   │   │   │   └── test_ufunclike.cpython-313.pyc
│   │   │   │   │   │   │   └── test_utils.cpython-313.pyc
│   │   │   │   │   │   ├── data/
│   │   │   │   │   │   │   └── py2-np0-objarr.npy
│   │   │   │   │   │   │   └── py2-objarr.npy
│   │   │   │   │   │   │   └── py2-objarr.npz
│   │   │   │   │   │   │   └── py3-objarr.npy
│   │   │   │   │   │   │   └── py3-objarr.npz
│   │   │   │   │   │   │   └── python3.npy
│   │   │   │   │   │   │   └── win64python2.npy
│   │   │   │   │   │   └── test__datasource.py
│   │   │   │   │   │   └── test__iotools.py
│   │   │   │   │   │   └── test__version.py
│   │   │   │   │   │   └── test_array_utils.py
│   │   │   │   │   │   └── test_arraypad.py
│   │   │   │   │   │   └── test_arraysetops.py
│   │   │   │   │   │   └── test_arrayterator.py
│   │   │   │   │   │   └── test_format.py
│   │   │   │   │   │   └── test_function_base.py
│   │   │   │   │   │   └── test_histograms.py
│   │   │   │   │   │   └── test_index_tricks.py
│   │   │   │   │   │   └── test_io.py
│   │   │   │   │   │   └── test_loadtxt.py
│   │   │   │   │   │   └── test_mixins.py
│   │   │   │   │   │   └── test_nanfunctions.py
│   │   │   │   │   │   └── test_packbits.py
│   │   │   │   │   │   └── test_polynomial.py
│   │   │   │   │   │   └── test_recfunctions.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   │   │   └── test_shape_base.py
│   │   │   │   │   │   └── test_stride_tricks.py
│   │   │   │   │   │   └── test_twodim_base.py
│   │   │   │   │   │   └── test_type_check.py
│   │   │   │   │   │   └── test_ufunclike.py
│   │   │   │   │   │   └── test_utils.py
│   │   │   │   │   └── user_array.py
│   │   │   │   │   └── user_array.pyi
│   │   │   │   ├── linalg/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _linalg.cpython-313.pyc
│   │   │   │   │   │   └── linalg.cpython-313.pyc
│   │   │   │   │   └── _linalg.py
│   │   │   │   │   └── _linalg.pyi
│   │   │   │   │   └── _umath_linalg.cp313-win_amd64.lib
│   │   │   │   │   └── _umath_linalg.cp313-win_amd64.pyd
│   │   │   │   │   └── _umath_linalg.pyi
│   │   │   │   │   └── lapack_lite.cp313-win_amd64.lib
│   │   │   │   │   └── lapack_lite.cp313-win_amd64.pyd
│   │   │   │   │   └── lapack_lite.pyi
│   │   │   │   │   └── linalg.py
│   │   │   │   │   └── linalg.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_deprecations.cpython-313.pyc
│   │   │   │   │   │   │   └── test_linalg.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   └── test_deprecations.py
│   │   │   │   │   │   └── test_linalg.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   ├── ma/
│   │   │   │   │   └── API_CHANGES.txt
│   │   │   │   │   └── LICENSE
│   │   │   │   │   └── README.rst
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── core.cpython-313.pyc
│   │   │   │   │   │   └── extras.cpython-313.pyc
│   │   │   │   │   │   └── mrecords.cpython-313.pyc
│   │   │   │   │   │   └── testutils.cpython-313.pyc
│   │   │   │   │   │   └── timer_comparison.cpython-313.pyc
│   │   │   │   │   └── core.py
│   │   │   │   │   └── core.pyi
│   │   │   │   │   └── extras.py
│   │   │   │   │   └── extras.pyi
│   │   │   │   │   └── mrecords.py
│   │   │   │   │   └── mrecords.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_arrayobject.cpython-313.pyc
│   │   │   │   │   │   │   └── test_core.cpython-313.pyc
│   │   │   │   │   │   │   └── test_deprecations.cpython-313.pyc
│   │   │   │   │   │   │   └── test_extras.cpython-313.pyc
│   │   │   │   │   │   │   └── test_mrecords.cpython-313.pyc
│   │   │   │   │   │   │   └── test_old_ma.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   │   └── test_subclassing.cpython-313.pyc
│   │   │   │   │   │   └── test_arrayobject.py
│   │   │   │   │   │   └── test_core.py
│   │   │   │   │   │   └── test_deprecations.py
│   │   │   │   │   │   └── test_extras.py
│   │   │   │   │   │   └── test_mrecords.py
│   │   │   │   │   │   └── test_old_ma.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   │   │   └── test_subclassing.py
│   │   │   │   │   └── testutils.py
│   │   │   │   │   └── timer_comparison.py
│   │   │   │   └── matlib.py
│   │   │   │   └── matlib.pyi
│   │   │   │   ├── matrixlib/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── defmatrix.cpython-313.pyc
│   │   │   │   │   └── defmatrix.py
│   │   │   │   │   └── defmatrix.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_defmatrix.cpython-313.pyc
│   │   │   │   │   │   │   └── test_interaction.cpython-313.pyc
│   │   │   │   │   │   │   └── test_masked_matrix.cpython-313.pyc
│   │   │   │   │   │   │   └── test_matrix_linalg.cpython-313.pyc
│   │   │   │   │   │   │   └── test_multiarray.cpython-313.pyc
│   │   │   │   │   │   │   └── test_numeric.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   └── test_defmatrix.py
│   │   │   │   │   │   └── test_interaction.py
│   │   │   │   │   │   └── test_masked_matrix.py
│   │   │   │   │   │   └── test_matrix_linalg.py
│   │   │   │   │   │   └── test_multiarray.py
│   │   │   │   │   │   └── test_numeric.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   ├── polynomial/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _polybase.cpython-313.pyc
│   │   │   │   │   │   └── chebyshev.cpython-313.pyc
│   │   │   │   │   │   └── hermite.cpython-313.pyc
│   │   │   │   │   │   └── hermite_e.cpython-313.pyc
│   │   │   │   │   │   └── laguerre.cpython-313.pyc
│   │   │   │   │   │   └── legendre.cpython-313.pyc
│   │   │   │   │   │   └── polynomial.cpython-313.pyc
│   │   │   │   │   │   └── polyutils.cpython-313.pyc
│   │   │   │   │   └── _polybase.py
│   │   │   │   │   └── _polybase.pyi
│   │   │   │   │   └── _polytypes.pyi
│   │   │   │   │   └── chebyshev.py
│   │   │   │   │   └── chebyshev.pyi
│   │   │   │   │   └── hermite.py
│   │   │   │   │   └── hermite.pyi
│   │   │   │   │   └── hermite_e.py
│   │   │   │   │   └── hermite_e.pyi
│   │   │   │   │   └── laguerre.py
│   │   │   │   │   └── laguerre.pyi
│   │   │   │   │   └── legendre.py
│   │   │   │   │   └── legendre.pyi
│   │   │   │   │   └── polynomial.py
│   │   │   │   │   └── polynomial.pyi
│   │   │   │   │   └── polyutils.py
│   │   │   │   │   └── polyutils.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_chebyshev.cpython-313.pyc
│   │   │   │   │   │   │   └── test_classes.cpython-313.pyc
│   │   │   │   │   │   │   └── test_hermite.cpython-313.pyc
│   │   │   │   │   │   │   └── test_hermite_e.cpython-313.pyc
│   │   │   │   │   │   │   └── test_laguerre.cpython-313.pyc
│   │   │   │   │   │   │   └── test_legendre.cpython-313.pyc
│   │   │   │   │   │   │   └── test_polynomial.cpython-313.pyc
│   │   │   │   │   │   │   └── test_polyutils.cpython-313.pyc
│   │   │   │   │   │   │   └── test_printing.cpython-313.pyc
│   │   │   │   │   │   │   └── test_symbol.cpython-313.pyc
│   │   │   │   │   │   └── test_chebyshev.py
│   │   │   │   │   │   └── test_classes.py
│   │   │   │   │   │   └── test_hermite.py
│   │   │   │   │   │   └── test_hermite_e.py
│   │   │   │   │   │   └── test_laguerre.py
│   │   │   │   │   │   └── test_legendre.py
│   │   │   │   │   │   └── test_polynomial.py
│   │   │   │   │   │   └── test_polyutils.py
│   │   │   │   │   │   └── test_printing.py
│   │   │   │   │   │   └── test_symbol.py
│   │   │   │   └── py.typed
│   │   │   │   ├── random/
│   │   │   │   │   └── LICENSE.md
│   │   │   │   │   └── __init__.pxd
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _pickle.cpython-313.pyc
│   │   │   │   │   └── _bounded_integers.cp313-win_amd64.lib
│   │   │   │   │   └── _bounded_integers.cp313-win_amd64.pyd
│   │   │   │   │   └── _bounded_integers.pxd
│   │   │   │   │   └── _common.cp313-win_amd64.lib
│   │   │   │   │   └── _common.cp313-win_amd64.pyd
│   │   │   │   │   └── _common.pxd
│   │   │   │   │   ├── _examples/
│   │   │   │   │   │   ├── cffi/
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── extending.cpython-313.pyc
│   │   │   │   │   │   │   │   └── parse.cpython-313.pyc
│   │   │   │   │   │   │   └── extending.py
│   │   │   │   │   │   │   └── parse.py
│   │   │   │   │   │   ├── cython/
│   │   │   │   │   │   │   └── extending.pyx
│   │   │   │   │   │   │   └── extending_distributions.pyx
│   │   │   │   │   │   │   └── meson.build
│   │   │   │   │   │   ├── numba/
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── extending.cpython-313.pyc
│   │   │   │   │   │   │   │   └── extending_distributions.cpython-313.pyc
│   │   │   │   │   │   │   └── extending.py
│   │   │   │   │   │   │   └── extending_distributions.py
│   │   │   │   │   └── _generator.cp313-win_amd64.lib
│   │   │   │   │   └── _generator.cp313-win_amd64.pyd
│   │   │   │   │   └── _generator.pyi
│   │   │   │   │   └── _mt19937.cp313-win_amd64.lib
│   │   │   │   │   └── _mt19937.cp313-win_amd64.pyd
│   │   │   │   │   └── _mt19937.pyi
│   │   │   │   │   └── _pcg64.cp313-win_amd64.lib
│   │   │   │   │   └── _pcg64.cp313-win_amd64.pyd
│   │   │   │   │   └── _pcg64.pyi
│   │   │   │   │   └── _philox.cp313-win_amd64.lib
│   │   │   │   │   └── _philox.cp313-win_amd64.pyd
│   │   │   │   │   └── _philox.pyi
│   │   │   │   │   └── _pickle.py
│   │   │   │   │   └── _pickle.pyi
│   │   │   │   │   └── _sfc64.cp313-win_amd64.lib
│   │   │   │   │   └── _sfc64.cp313-win_amd64.pyd
│   │   │   │   │   └── _sfc64.pyi
│   │   │   │   │   └── bit_generator.cp313-win_amd64.lib
│   │   │   │   │   └── bit_generator.cp313-win_amd64.pyd
│   │   │   │   │   └── bit_generator.pxd
│   │   │   │   │   └── bit_generator.pyi
│   │   │   │   │   └── c_distributions.pxd
│   │   │   │   │   ├── lib/
│   │   │   │   │   │   └── npyrandom.lib
│   │   │   │   │   └── mtrand.cp313-win_amd64.lib
│   │   │   │   │   └── mtrand.cp313-win_amd64.pyd
│   │   │   │   │   └── mtrand.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_direct.cpython-313.pyc
│   │   │   │   │   │   │   └── test_extending.cpython-313.pyc
│   │   │   │   │   │   │   └── test_generator_mt19937.cpython-313.pyc
│   │   │   │   │   │   │   └── test_generator_mt19937_regressions.cpython-313.pyc
│   │   │   │   │   │   │   └── test_random.cpython-313.pyc
│   │   │   │   │   │   │   └── test_randomstate.cpython-313.pyc
│   │   │   │   │   │   │   └── test_randomstate_regression.cpython-313.pyc
│   │   │   │   │   │   │   └── test_regression.cpython-313.pyc
│   │   │   │   │   │   │   └── test_seed_sequence.cpython-313.pyc
│   │   │   │   │   │   │   └── test_smoke.cpython-313.pyc
│   │   │   │   │   │   ├── data/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── generator_pcg64_np121.pkl.gz
│   │   │   │   │   │   │   └── generator_pcg64_np126.pkl.gz
│   │   │   │   │   │   │   └── mt19937-testset-1.csv
│   │   │   │   │   │   │   └── mt19937-testset-2.csv
│   │   │   │   │   │   │   └── pcg64-testset-1.csv
│   │   │   │   │   │   │   └── pcg64-testset-2.csv
│   │   │   │   │   │   │   └── pcg64dxsm-testset-1.csv
│   │   │   │   │   │   │   └── pcg64dxsm-testset-2.csv
│   │   │   │   │   │   │   └── philox-testset-1.csv
│   │   │   │   │   │   │   └── philox-testset-2.csv
│   │   │   │   │   │   │   └── sfc64-testset-1.csv
│   │   │   │   │   │   │   └── sfc64-testset-2.csv
│   │   │   │   │   │   │   └── sfc64_np126.pkl.gz
│   │   │   │   │   │   └── test_direct.py
│   │   │   │   │   │   └── test_extending.py
│   │   │   │   │   │   └── test_generator_mt19937.py
│   │   │   │   │   │   └── test_generator_mt19937_regressions.py
│   │   │   │   │   │   └── test_random.py
│   │   │   │   │   │   └── test_randomstate.py
│   │   │   │   │   │   └── test_randomstate_regression.py
│   │   │   │   │   │   └── test_regression.py
│   │   │   │   │   │   └── test_seed_sequence.py
│   │   │   │   │   │   └── test_smoke.py
│   │   │   │   ├── rec/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   ├── strings/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   ├── testing/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.pyi
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── overrides.cpython-313.pyc
│   │   │   │   │   │   └── print_coercion_tables.cpython-313.pyc
│   │   │   │   │   ├── _private/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── __init__.pyi
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── extbuild.cpython-313.pyc
│   │   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   └── extbuild.py
│   │   │   │   │   │   └── extbuild.pyi
│   │   │   │   │   │   └── utils.py
│   │   │   │   │   │   └── utils.pyi
│   │   │   │   │   └── overrides.py
│   │   │   │   │   └── overrides.pyi
│   │   │   │   │   └── print_coercion_tables.py
│   │   │   │   │   └── print_coercion_tables.pyi
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_utils.cpython-313.pyc
│   │   │   │   │   │   └── test_utils.py
│   │   │   │   ├── tests/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── test__all__.cpython-313.pyc
│   │   │   │   │   │   └── test_configtool.cpython-313.pyc
│   │   │   │   │   │   └── test_ctypeslib.cpython-313.pyc
│   │   │   │   │   │   └── test_lazyloading.cpython-313.pyc
│   │   │   │   │   │   └── test_matlib.cpython-313.pyc
│   │   │   │   │   │   └── test_numpy_config.cpython-313.pyc
│   │   │   │   │   │   └── test_numpy_version.cpython-313.pyc
│   │   │   │   │   │   └── test_public_api.cpython-313.pyc
│   │   │   │   │   │   └── test_reloading.cpython-313.pyc
│   │   │   │   │   │   └── test_scripts.cpython-313.pyc
│   │   │   │   │   │   └── test_warnings.cpython-313.pyc
│   │   │   │   │   └── test__all__.py
│   │   │   │   │   └── test_configtool.py
│   │   │   │   │   └── test_ctypeslib.py
│   │   │   │   │   └── test_lazyloading.py
│   │   │   │   │   └── test_matlib.py
│   │   │   │   │   └── test_numpy_config.py
│   │   │   │   │   └── test_numpy_version.py
│   │   │   │   │   └── test_public_api.py
│   │   │   │   │   └── test_reloading.py
│   │   │   │   │   └── test_scripts.py
│   │   │   │   │   └── test_warnings.py
│   │   │   │   ├── typing/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── mypy_plugin.cpython-313.pyc
│   │   │   │   │   └── mypy_plugin.py
│   │   │   │   │   ├── tests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── test_isfile.cpython-313.pyc
│   │   │   │   │   │   │   └── test_runtime.cpython-313.pyc
│   │   │   │   │   │   │   └── test_typing.cpython-313.pyc
│   │   │   │   │   │   ├── data/
│   │   │   │   │   │   │   ├── fail/
│   │   │   │   │   │   │   │   └── arithmetic.pyi
│   │   │   │   │   │   │   │   └── array_constructors.pyi
│   │   │   │   │   │   │   │   └── array_like.pyi
│   │   │   │   │   │   │   │   └── array_pad.pyi
│   │   │   │   │   │   │   │   └── arrayprint.pyi
│   │   │   │   │   │   │   │   └── arrayterator.pyi
│   │   │   │   │   │   │   │   └── bitwise_ops.pyi
│   │   │   │   │   │   │   │   └── char.pyi
│   │   │   │   │   │   │   │   └── chararray.pyi
│   │   │   │   │   │   │   │   └── comparisons.pyi
│   │   │   │   │   │   │   │   └── constants.pyi
│   │   │   │   │   │   │   │   └── datasource.pyi
│   │   │   │   │   │   │   │   └── dtype.pyi
│   │   │   │   │   │   │   │   └── einsumfunc.pyi
│   │   │   │   │   │   │   │   └── flatiter.pyi
│   │   │   │   │   │   │   │   └── fromnumeric.pyi
│   │   │   │   │   │   │   │   └── histograms.pyi
│   │   │   │   │   │   │   │   └── index_tricks.pyi
│   │   │   │   │   │   │   │   └── lib_function_base.pyi
│   │   │   │   │   │   │   │   └── lib_polynomial.pyi
│   │   │   │   │   │   │   │   └── lib_utils.pyi
│   │   │   │   │   │   │   │   └── lib_version.pyi
│   │   │   │   │   │   │   │   └── linalg.pyi
│   │   │   │   │   │   │   │   └── memmap.pyi
│   │   │   │   │   │   │   │   └── modules.pyi
│   │   │   │   │   │   │   │   └── multiarray.pyi
│   │   │   │   │   │   │   │   └── ndarray.pyi
│   │   │   │   │   │   │   │   └── ndarray_misc.pyi
│   │   │   │   │   │   │   │   └── nditer.pyi
│   │   │   │   │   │   │   │   └── nested_sequence.pyi
│   │   │   │   │   │   │   │   └── npyio.pyi
│   │   │   │   │   │   │   │   └── numerictypes.pyi
│   │   │   │   │   │   │   │   └── random.pyi
│   │   │   │   │   │   │   │   └── rec.pyi
│   │   │   │   │   │   │   │   └── scalars.pyi
│   │   │   │   │   │   │   │   └── shape.pyi
│   │   │   │   │   │   │   │   └── shape_base.pyi
│   │   │   │   │   │   │   │   └── stride_tricks.pyi
│   │   │   │   │   │   │   │   └── strings.pyi
│   │   │   │   │   │   │   │   └── testing.pyi
│   │   │   │   │   │   │   │   └── twodim_base.pyi
│   │   │   │   │   │   │   │   └── type_check.pyi
│   │   │   │   │   │   │   │   └── ufunc_config.pyi
│   │   │   │   │   │   │   │   └── ufunclike.pyi
│   │   │   │   │   │   │   │   └── ufuncs.pyi
│   │   │   │   │   │   │   │   └── warnings_and_errors.pyi
│   │   │   │   │   │   │   ├── misc/
│   │   │   │   │   │   │   │   └── extended_precision.pyi
│   │   │   │   │   │   │   └── mypy.ini
│   │   │   │   │   │   │   ├── pass/
│   │   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   │   └── arithmetic.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── array_constructors.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── array_like.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── arrayprint.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── arrayterator.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── bitwise_ops.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── comparisons.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── dtype.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── einsumfunc.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── flatiter.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── fromnumeric.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── index_tricks.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── lib_user_array.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── lib_utils.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── lib_version.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── literal.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ma.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── mod.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── modules.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── multiarray.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ndarray_conversion.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ndarray_misc.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ndarray_shape_manipulation.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── nditer.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── numeric.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── numerictypes.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── random.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── recfunctions.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── scalars.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── shape.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── simple.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── simple_py3.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ufunc_config.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ufunclike.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── ufuncs.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── warnings_and_errors.cpython-313.pyc
│   │   │   │   │   │   │   │   └── arithmetic.py
│   │   │   │   │   │   │   │   └── array_constructors.py
│   │   │   │   │   │   │   │   └── array_like.py
│   │   │   │   │   │   │   │   └── arrayprint.py
│   │   │   │   │   │   │   │   └── arrayterator.py
│   │   │   │   │   │   │   │   └── bitwise_ops.py
│   │   │   │   │   │   │   │   └── comparisons.py
│   │   │   │   │   │   │   │   └── dtype.py
│   │   │   │   │   │   │   │   └── einsumfunc.py
│   │   │   │   │   │   │   │   └── flatiter.py
│   │   │   │   │   │   │   │   └── fromnumeric.py
│   │   │   │   │   │   │   │   └── index_tricks.py
│   │   │   │   │   │   │   │   └── lib_user_array.py
│   │   │   │   │   │   │   │   └── lib_utils.py
│   │   │   │   │   │   │   │   └── lib_version.py
│   │   │   │   │   │   │   │   └── literal.py
│   │   │   │   │   │   │   │   └── ma.py
│   │   │   │   │   │   │   │   └── mod.py
│   │   │   │   │   │   │   │   └── modules.py
│   │   │   │   │   │   │   │   └── multiarray.py
│   │   │   │   │   │   │   │   └── ndarray_conversion.py
│   │   │   │   │   │   │   │   └── ndarray_misc.py
│   │   │   │   │   │   │   │   └── ndarray_shape_manipulation.py
│   │   │   │   │   │   │   │   └── nditer.py
│   │   │   │   │   │   │   │   └── numeric.py
│   │   │   │   │   │   │   │   └── numerictypes.py
│   │   │   │   │   │   │   │   └── random.py
│   │   │   │   │   │   │   │   └── recfunctions.py
│   │   │   │   │   │   │   │   └── scalars.py
│   │   │   │   │   │   │   │   └── shape.py
│   │   │   │   │   │   │   │   └── simple.py
│   │   │   │   │   │   │   │   └── simple_py3.py
│   │   │   │   │   │   │   │   └── ufunc_config.py
│   │   │   │   │   │   │   │   └── ufunclike.py
│   │   │   │   │   │   │   │   └── ufuncs.py
│   │   │   │   │   │   │   │   └── warnings_and_errors.py
│   │   │   │   │   │   │   ├── reveal/
│   │   │   │   │   │   │   │   └── arithmetic.pyi
│   │   │   │   │   │   │   │   └── array_api_info.pyi
│   │   │   │   │   │   │   │   └── array_constructors.pyi
│   │   │   │   │   │   │   │   └── arraypad.pyi
│   │   │   │   │   │   │   │   └── arrayprint.pyi
│   │   │   │   │   │   │   │   └── arraysetops.pyi
│   │   │   │   │   │   │   │   └── arrayterator.pyi
│   │   │   │   │   │   │   │   └── bitwise_ops.pyi
│   │   │   │   │   │   │   │   └── char.pyi
│   │   │   │   │   │   │   │   └── chararray.pyi
│   │   │   │   │   │   │   │   └── comparisons.pyi
│   │   │   │   │   │   │   │   └── constants.pyi
│   │   │   │   │   │   │   │   └── ctypeslib.pyi
│   │   │   │   │   │   │   │   └── datasource.pyi
│   │   │   │   │   │   │   │   └── dtype.pyi
│   │   │   │   │   │   │   │   └── einsumfunc.pyi
│   │   │   │   │   │   │   │   └── emath.pyi
│   │   │   │   │   │   │   │   └── fft.pyi
│   │   │   │   │   │   │   │   └── flatiter.pyi
│   │   │   │   │   │   │   │   └── fromnumeric.pyi
│   │   │   │   │   │   │   │   └── getlimits.pyi
│   │   │   │   │   │   │   │   └── histograms.pyi
│   │   │   │   │   │   │   │   └── index_tricks.pyi
│   │   │   │   │   │   │   │   └── lib_function_base.pyi
│   │   │   │   │   │   │   │   └── lib_polynomial.pyi
│   │   │   │   │   │   │   │   └── lib_utils.pyi
│   │   │   │   │   │   │   │   └── lib_version.pyi
│   │   │   │   │   │   │   │   └── linalg.pyi
│   │   │   │   │   │   │   │   └── matrix.pyi
│   │   │   │   │   │   │   │   └── memmap.pyi
│   │   │   │   │   │   │   │   └── mod.pyi
│   │   │   │   │   │   │   │   └── modules.pyi
│   │   │   │   │   │   │   │   └── multiarray.pyi
│   │   │   │   │   │   │   │   └── nbit_base_example.pyi
│   │   │   │   │   │   │   │   └── ndarray_assignability.pyi
│   │   │   │   │   │   │   │   └── ndarray_conversion.pyi
│   │   │   │   │   │   │   │   └── ndarray_misc.pyi
│   │   │   │   │   │   │   │   └── ndarray_shape_manipulation.pyi
│   │   │   │   │   │   │   │   └── nditer.pyi
│   │   │   │   │   │   │   │   └── nested_sequence.pyi
│   │   │   │   │   │   │   │   └── npyio.pyi
│   │   │   │   │   │   │   │   └── numeric.pyi
│   │   │   │   │   │   │   │   └── numerictypes.pyi
│   │   │   │   │   │   │   │   └── polynomial_polybase.pyi
│   │   │   │   │   │   │   │   └── polynomial_polyutils.pyi
│   │   │   │   │   │   │   │   └── polynomial_series.pyi
│   │   │   │   │   │   │   │   └── random.pyi
│   │   │   │   │   │   │   │   └── rec.pyi
│   │   │   │   │   │   │   │   └── scalars.pyi
│   │   │   │   │   │   │   │   └── shape.pyi
│   │   │   │   │   │   │   │   └── shape_base.pyi
│   │   │   │   │   │   │   │   └── stride_tricks.pyi
│   │   │   │   │   │   │   │   └── strings.pyi
│   │   │   │   │   │   │   │   └── testing.pyi
│   │   │   │   │   │   │   │   └── twodim_base.pyi
│   │   │   │   │   │   │   │   └── type_check.pyi
│   │   │   │   │   │   │   │   └── ufunc_config.pyi
│   │   │   │   │   │   │   │   └── ufunclike.pyi
│   │   │   │   │   │   │   │   └── ufuncs.pyi
│   │   │   │   │   │   │   │   └── warnings_and_errors.pyi
│   │   │   │   │   │   └── test_isfile.py
│   │   │   │   │   │   └── test_runtime.py
│   │   │   │   │   │   └── test_typing.py
│   │   │   │   └── version.py
│   │   │   │   └── version.pyi
│   │   │   └── numpy-2.2.4-cp313-cp313-win_amd64.whl
│   │   │   ├── numpy-2.2.4.dist-info/
│   │   │   │   └── DELVEWHEEL
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   ├── numpy.libs/
│   │   │   │   └── libscipy_openblas64_-43e11ff0749b8cbe0a615c9cf6737e0e.dll
│   │   │   │   └── msvcp140-263139962577ecda4cd9469ca360a746.dll
│   │   │   ├── onvif/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── cli.cpython-313.pyc
│   │   │   │   │   └── client.cpython-313.pyc
│   │   │   │   │   └── definition.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   └── cli.py
│   │   │   │   └── client.py
│   │   │   │   └── definition.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── version.txt
│   │   │   ├── onvif_zeep-0.2.12.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE
│   │   │   │   └── top_level.txt
│   │   │   ├── opencv_python-4.11.0.86.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE-3RD-PARTY.txt
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── pillow-11.1.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   │   └── zip-safe
│   │   │   ├── pip/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   └── __pip-runner__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── __pip-runner__.cpython-313.pyc
│   │   │   │   ├── _internal/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── build_env.cpython-313.pyc
│   │   │   │   │   │   └── cache.cpython-313.pyc
│   │   │   │   │   │   └── configuration.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   └── main.cpython-313.pyc
│   │   │   │   │   │   └── pyproject.cpython-313.pyc
│   │   │   │   │   │   └── self_outdated_check.cpython-313.pyc
│   │   │   │   │   │   └── wheel_builder.cpython-313.pyc
│   │   │   │   │   └── build_env.py
│   │   │   │   │   └── cache.py
│   │   │   │   │   ├── cli/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── autocompletion.cpython-313.pyc
│   │   │   │   │   │   │   └── base_command.cpython-313.pyc
│   │   │   │   │   │   │   └── cmdoptions.cpython-313.pyc
│   │   │   │   │   │   │   └── command_context.cpython-313.pyc
│   │   │   │   │   │   │   └── index_command.cpython-313.pyc
│   │   │   │   │   │   │   └── main.cpython-313.pyc
│   │   │   │   │   │   │   └── main_parser.cpython-313.pyc
│   │   │   │   │   │   │   └── parser.cpython-313.pyc
│   │   │   │   │   │   │   └── progress_bars.cpython-313.pyc
│   │   │   │   │   │   │   └── req_command.cpython-313.pyc
│   │   │   │   │   │   │   └── spinners.cpython-313.pyc
│   │   │   │   │   │   │   └── status_codes.cpython-313.pyc
│   │   │   │   │   │   └── autocompletion.py
│   │   │   │   │   │   └── base_command.py
│   │   │   │   │   │   └── cmdoptions.py
│   │   │   │   │   │   └── command_context.py
│   │   │   │   │   │   └── index_command.py
│   │   │   │   │   │   └── main.py
│   │   │   │   │   │   └── main_parser.py
│   │   │   │   │   │   └── parser.py
│   │   │   │   │   │   └── progress_bars.py
│   │   │   │   │   │   └── req_command.py
│   │   │   │   │   │   └── spinners.py
│   │   │   │   │   │   └── status_codes.py
│   │   │   │   │   ├── commands/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── cache.cpython-313.pyc
│   │   │   │   │   │   │   └── check.cpython-313.pyc
│   │   │   │   │   │   │   └── completion.cpython-313.pyc
│   │   │   │   │   │   │   └── configuration.cpython-313.pyc
│   │   │   │   │   │   │   └── debug.cpython-313.pyc
│   │   │   │   │   │   │   └── download.cpython-313.pyc
│   │   │   │   │   │   │   └── freeze.cpython-313.pyc
│   │   │   │   │   │   │   └── hash.cpython-313.pyc
│   │   │   │   │   │   │   └── help.cpython-313.pyc
│   │   │   │   │   │   │   └── index.cpython-313.pyc
│   │   │   │   │   │   │   └── inspect.cpython-313.pyc
│   │   │   │   │   │   │   └── install.cpython-313.pyc
│   │   │   │   │   │   │   └── list.cpython-313.pyc
│   │   │   │   │   │   │   └── search.cpython-313.pyc
│   │   │   │   │   │   │   └── show.cpython-313.pyc
│   │   │   │   │   │   │   └── uninstall.cpython-313.pyc
│   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   └── cache.py
│   │   │   │   │   │   └── check.py
│   │   │   │   │   │   └── completion.py
│   │   │   │   │   │   └── configuration.py
│   │   │   │   │   │   └── debug.py
│   │   │   │   │   │   └── download.py
│   │   │   │   │   │   └── freeze.py
│   │   │   │   │   │   └── hash.py
│   │   │   │   │   │   └── help.py
│   │   │   │   │   │   └── index.py
│   │   │   │   │   │   └── inspect.py
│   │   │   │   │   │   └── install.py
│   │   │   │   │   │   └── list.py
│   │   │   │   │   │   └── search.py
│   │   │   │   │   │   └── show.py
│   │   │   │   │   │   └── uninstall.py
│   │   │   │   │   │   └── wheel.py
│   │   │   │   │   └── configuration.py
│   │   │   │   │   ├── distributions/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   │   └── installed.cpython-313.pyc
│   │   │   │   │   │   │   └── sdist.cpython-313.pyc
│   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   └── base.py
│   │   │   │   │   │   └── installed.py
│   │   │   │   │   │   └── sdist.py
│   │   │   │   │   │   └── wheel.py
│   │   │   │   │   └── exceptions.py
│   │   │   │   │   ├── index/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── collector.cpython-313.pyc
│   │   │   │   │   │   │   └── package_finder.cpython-313.pyc
│   │   │   │   │   │   │   └── sources.cpython-313.pyc
│   │   │   │   │   │   └── collector.py
│   │   │   │   │   │   └── package_finder.py
│   │   │   │   │   │   └── sources.py
│   │   │   │   │   ├── locations/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _distutils.cpython-313.pyc
│   │   │   │   │   │   │   └── _sysconfig.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   └── _distutils.py
│   │   │   │   │   │   └── _sysconfig.py
│   │   │   │   │   │   └── base.py
│   │   │   │   │   └── main.py
│   │   │   │   │   ├── metadata/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _json.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   │   └── pkg_resources.cpython-313.pyc
│   │   │   │   │   │   └── _json.py
│   │   │   │   │   │   └── base.py
│   │   │   │   │   │   ├── importlib/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _compat.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _dists.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _envs.cpython-313.pyc
│   │   │   │   │   │   │   └── _compat.py
│   │   │   │   │   │   │   └── _dists.py
│   │   │   │   │   │   │   └── _envs.py
│   │   │   │   │   │   └── pkg_resources.py
│   │   │   │   │   ├── models/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── candidate.cpython-313.pyc
│   │   │   │   │   │   │   └── direct_url.cpython-313.pyc
│   │   │   │   │   │   │   └── format_control.cpython-313.pyc
│   │   │   │   │   │   │   └── index.cpython-313.pyc
│   │   │   │   │   │   │   └── installation_report.cpython-313.pyc
│   │   │   │   │   │   │   └── link.cpython-313.pyc
│   │   │   │   │   │   │   └── scheme.cpython-313.pyc
│   │   │   │   │   │   │   └── search_scope.cpython-313.pyc
│   │   │   │   │   │   │   └── selection_prefs.cpython-313.pyc
│   │   │   │   │   │   │   └── target_python.cpython-313.pyc
│   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   └── candidate.py
│   │   │   │   │   │   └── direct_url.py
│   │   │   │   │   │   └── format_control.py
│   │   │   │   │   │   └── index.py
│   │   │   │   │   │   └── installation_report.py
│   │   │   │   │   │   └── link.py
│   │   │   │   │   │   └── scheme.py
│   │   │   │   │   │   └── search_scope.py
│   │   │   │   │   │   └── selection_prefs.py
│   │   │   │   │   │   └── target_python.py
│   │   │   │   │   │   └── wheel.py
│   │   │   │   │   ├── network/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── auth.cpython-313.pyc
│   │   │   │   │   │   │   └── cache.cpython-313.pyc
│   │   │   │   │   │   │   └── download.cpython-313.pyc
│   │   │   │   │   │   │   └── lazy_wheel.cpython-313.pyc
│   │   │   │   │   │   │   └── session.cpython-313.pyc
│   │   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   │   └── xmlrpc.cpython-313.pyc
│   │   │   │   │   │   └── auth.py
│   │   │   │   │   │   └── cache.py
│   │   │   │   │   │   └── download.py
│   │   │   │   │   │   └── lazy_wheel.py
│   │   │   │   │   │   └── session.py
│   │   │   │   │   │   └── utils.py
│   │   │   │   │   │   └── xmlrpc.py
│   │   │   │   │   ├── operations/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── check.cpython-313.pyc
│   │   │   │   │   │   │   └── freeze.cpython-313.pyc
│   │   │   │   │   │   │   └── prepare.cpython-313.pyc
│   │   │   │   │   │   ├── build/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── build_tracker.cpython-313.pyc
│   │   │   │   │   │   │   │   └── metadata.cpython-313.pyc
│   │   │   │   │   │   │   │   └── metadata_editable.cpython-313.pyc
│   │   │   │   │   │   │   │   └── metadata_legacy.cpython-313.pyc
│   │   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   │   │   └── wheel_editable.cpython-313.pyc
│   │   │   │   │   │   │   │   └── wheel_legacy.cpython-313.pyc
│   │   │   │   │   │   │   └── build_tracker.py
│   │   │   │   │   │   │   └── metadata.py
│   │   │   │   │   │   │   └── metadata_editable.py
│   │   │   │   │   │   │   └── metadata_legacy.py
│   │   │   │   │   │   │   └── wheel.py
│   │   │   │   │   │   │   └── wheel_editable.py
│   │   │   │   │   │   │   └── wheel_legacy.py
│   │   │   │   │   │   └── check.py
│   │   │   │   │   │   └── freeze.py
│   │   │   │   │   │   ├── install/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── editable_legacy.cpython-313.pyc
│   │   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   │   └── editable_legacy.py
│   │   │   │   │   │   │   └── wheel.py
│   │   │   │   │   │   └── prepare.py
│   │   │   │   │   └── pyproject.py
│   │   │   │   │   ├── req/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── constructors.cpython-313.pyc
│   │   │   │   │   │   │   └── req_file.cpython-313.pyc
│   │   │   │   │   │   │   └── req_install.cpython-313.pyc
│   │   │   │   │   │   │   └── req_set.cpython-313.pyc
│   │   │   │   │   │   │   └── req_uninstall.cpython-313.pyc
│   │   │   │   │   │   └── constructors.py
│   │   │   │   │   │   └── req_file.py
│   │   │   │   │   │   └── req_install.py
│   │   │   │   │   │   └── req_set.py
│   │   │   │   │   │   └── req_uninstall.py
│   │   │   │   │   ├── resolution/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   └── base.py
│   │   │   │   │   │   ├── legacy/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── resolver.cpython-313.pyc
│   │   │   │   │   │   │   └── resolver.py
│   │   │   │   │   │   ├── resolvelib/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   │   │   └── candidates.cpython-313.pyc
│   │   │   │   │   │   │   │   └── factory.cpython-313.pyc
│   │   │   │   │   │   │   │   └── found_candidates.cpython-313.pyc
│   │   │   │   │   │   │   │   └── provider.cpython-313.pyc
│   │   │   │   │   │   │   │   └── reporter.cpython-313.pyc
│   │   │   │   │   │   │   │   └── requirements.cpython-313.pyc
│   │   │   │   │   │   │   │   └── resolver.cpython-313.pyc
│   │   │   │   │   │   │   └── base.py
│   │   │   │   │   │   │   └── candidates.py
│   │   │   │   │   │   │   └── factory.py
│   │   │   │   │   │   │   └── found_candidates.py
│   │   │   │   │   │   │   └── provider.py
│   │   │   │   │   │   │   └── reporter.py
│   │   │   │   │   │   │   └── requirements.py
│   │   │   │   │   │   │   └── resolver.py
│   │   │   │   │   └── self_outdated_check.py
│   │   │   │   │   ├── utils/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _jaraco_text.cpython-313.pyc
│   │   │   │   │   │   │   └── _log.cpython-313.pyc
│   │   │   │   │   │   │   └── appdirs.cpython-313.pyc
│   │   │   │   │   │   │   └── compat.cpython-313.pyc
│   │   │   │   │   │   │   └── compatibility_tags.cpython-313.pyc
│   │   │   │   │   │   │   └── datetime.cpython-313.pyc
│   │   │   │   │   │   │   └── deprecation.cpython-313.pyc
│   │   │   │   │   │   │   └── direct_url_helpers.cpython-313.pyc
│   │   │   │   │   │   │   └── egg_link.cpython-313.pyc
│   │   │   │   │   │   │   └── entrypoints.cpython-313.pyc
│   │   │   │   │   │   │   └── filesystem.cpython-313.pyc
│   │   │   │   │   │   │   └── filetypes.cpython-313.pyc
│   │   │   │   │   │   │   └── glibc.cpython-313.pyc
│   │   │   │   │   │   │   └── hashes.cpython-313.pyc
│   │   │   │   │   │   │   └── logging.cpython-313.pyc
│   │   │   │   │   │   │   └── misc.cpython-313.pyc
│   │   │   │   │   │   │   └── packaging.cpython-313.pyc
│   │   │   │   │   │   │   └── retry.cpython-313.pyc
│   │   │   │   │   │   │   └── setuptools_build.cpython-313.pyc
│   │   │   │   │   │   │   └── subprocess.cpython-313.pyc
│   │   │   │   │   │   │   └── temp_dir.cpython-313.pyc
│   │   │   │   │   │   │   └── unpacking.cpython-313.pyc
│   │   │   │   │   │   │   └── urls.cpython-313.pyc
│   │   │   │   │   │   │   └── virtualenv.cpython-313.pyc
│   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   └── _jaraco_text.py
│   │   │   │   │   │   └── _log.py
│   │   │   │   │   │   └── appdirs.py
│   │   │   │   │   │   └── compat.py
│   │   │   │   │   │   └── compatibility_tags.py
│   │   │   │   │   │   └── datetime.py
│   │   │   │   │   │   └── deprecation.py
│   │   │   │   │   │   └── direct_url_helpers.py
│   │   │   │   │   │   └── egg_link.py
│   │   │   │   │   │   └── entrypoints.py
│   │   │   │   │   │   └── filesystem.py
│   │   │   │   │   │   └── filetypes.py
│   │   │   │   │   │   └── glibc.py
│   │   │   │   │   │   └── hashes.py
│   │   │   │   │   │   └── logging.py
│   │   │   │   │   │   └── misc.py
│   │   │   │   │   │   └── packaging.py
│   │   │   │   │   │   └── retry.py
│   │   │   │   │   │   └── setuptools_build.py
│   │   │   │   │   │   └── subprocess.py
│   │   │   │   │   │   └── temp_dir.py
│   │   │   │   │   │   └── unpacking.py
│   │   │   │   │   │   └── urls.py
│   │   │   │   │   │   └── virtualenv.py
│   │   │   │   │   │   └── wheel.py
│   │   │   │   │   ├── vcs/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── bazaar.cpython-313.pyc
│   │   │   │   │   │   │   └── git.cpython-313.pyc
│   │   │   │   │   │   │   └── mercurial.cpython-313.pyc
│   │   │   │   │   │   │   └── subversion.cpython-313.pyc
│   │   │   │   │   │   │   └── versioncontrol.cpython-313.pyc
│   │   │   │   │   │   └── bazaar.py
│   │   │   │   │   │   └── git.py
│   │   │   │   │   │   └── mercurial.py
│   │   │   │   │   │   └── subversion.py
│   │   │   │   │   │   └── versioncontrol.py
│   │   │   │   │   └── wheel_builder.py
│   │   │   │   ├── _vendor/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── typing_extensions.cpython-313.pyc
│   │   │   │   │   ├── cachecontrol/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _cmd.cpython-313.pyc
│   │   │   │   │   │   │   └── adapter.cpython-313.pyc
│   │   │   │   │   │   │   └── cache.cpython-313.pyc
│   │   │   │   │   │   │   └── controller.cpython-313.pyc
│   │   │   │   │   │   │   └── filewrapper.cpython-313.pyc
│   │   │   │   │   │   │   └── heuristics.cpython-313.pyc
│   │   │   │   │   │   │   └── serialize.cpython-313.pyc
│   │   │   │   │   │   │   └── wrapper.cpython-313.pyc
│   │   │   │   │   │   └── _cmd.py
│   │   │   │   │   │   └── adapter.py
│   │   │   │   │   │   └── cache.py
│   │   │   │   │   │   ├── caches/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── file_cache.cpython-313.pyc
│   │   │   │   │   │   │   │   └── redis_cache.cpython-313.pyc
│   │   │   │   │   │   │   └── file_cache.py
│   │   │   │   │   │   │   └── redis_cache.py
│   │   │   │   │   │   └── controller.py
│   │   │   │   │   │   └── filewrapper.py
│   │   │   │   │   │   └── heuristics.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   │   └── serialize.py
│   │   │   │   │   │   └── wrapper.py
│   │   │   │   │   ├── certifi/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── __main__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   │   │   └── core.cpython-313.pyc
│   │   │   │   │   │   └── cacert.pem
│   │   │   │   │   │   └── core.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   ├── distlib/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── compat.cpython-313.pyc
│   │   │   │   │   │   │   └── database.cpython-313.pyc
│   │   │   │   │   │   │   └── index.cpython-313.pyc
│   │   │   │   │   │   │   └── locators.cpython-313.pyc
│   │   │   │   │   │   │   └── manifest.cpython-313.pyc
│   │   │   │   │   │   │   └── markers.cpython-313.pyc
│   │   │   │   │   │   │   └── metadata.cpython-313.pyc
│   │   │   │   │   │   │   └── resources.cpython-313.pyc
│   │   │   │   │   │   │   └── scripts.cpython-313.pyc
│   │   │   │   │   │   │   └── util.cpython-313.pyc
│   │   │   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   │   │   │   └── wheel.cpython-313.pyc
│   │   │   │   │   │   └── compat.py
│   │   │   │   │   │   └── database.py
│   │   │   │   │   │   └── index.py
│   │   │   │   │   │   └── locators.py
│   │   │   │   │   │   └── manifest.py
│   │   │   │   │   │   └── markers.py
│   │   │   │   │   │   └── metadata.py
│   │   │   │   │   │   └── resources.py
│   │   │   │   │   │   └── scripts.py
│   │   │   │   │   │   └── t32.exe
│   │   │   │   │   │   └── t64-arm.exe
│   │   │   │   │   │   └── t64.exe
│   │   │   │   │   │   └── util.py
│   │   │   │   │   │   └── version.py
│   │   │   │   │   │   └── w32.exe
│   │   │   │   │   │   └── w64-arm.exe
│   │   │   │   │   │   └── w64.exe
│   │   │   │   │   │   └── wheel.py
│   │   │   │   │   ├── distro/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── __main__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   │   │   └── distro.cpython-313.pyc
│   │   │   │   │   │   └── distro.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   ├── idna/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── codec.cpython-313.pyc
│   │   │   │   │   │   │   └── compat.cpython-313.pyc
│   │   │   │   │   │   │   └── core.cpython-313.pyc
│   │   │   │   │   │   │   └── idnadata.cpython-313.pyc
│   │   │   │   │   │   │   └── intranges.cpython-313.pyc
│   │   │   │   │   │   │   └── package_data.cpython-313.pyc
│   │   │   │   │   │   │   └── uts46data.cpython-313.pyc
│   │   │   │   │   │   └── codec.py
│   │   │   │   │   │   └── compat.py
│   │   │   │   │   │   └── core.py
│   │   │   │   │   │   └── idnadata.py
│   │   │   │   │   │   └── intranges.py
│   │   │   │   │   │   └── package_data.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   │   └── uts46data.py
│   │   │   │   │   ├── msgpack/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   │   └── ext.cpython-313.pyc
│   │   │   │   │   │   │   └── fallback.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.py
│   │   │   │   │   │   └── ext.py
│   │   │   │   │   │   └── fallback.py
│   │   │   │   │   ├── packaging/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _elffile.cpython-313.pyc
│   │   │   │   │   │   │   └── _manylinux.cpython-313.pyc
│   │   │   │   │   │   │   └── _musllinux.cpython-313.pyc
│   │   │   │   │   │   │   └── _parser.cpython-313.pyc
│   │   │   │   │   │   │   └── _structures.cpython-313.pyc
│   │   │   │   │   │   │   └── _tokenizer.cpython-313.pyc
│   │   │   │   │   │   │   └── markers.cpython-313.pyc
│   │   │   │   │   │   │   └── metadata.cpython-313.pyc
│   │   │   │   │   │   │   └── requirements.cpython-313.pyc
│   │   │   │   │   │   │   └── specifiers.cpython-313.pyc
│   │   │   │   │   │   │   └── tags.cpython-313.pyc
│   │   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   │   │   └── _elffile.py
│   │   │   │   │   │   └── _manylinux.py
│   │   │   │   │   │   └── _musllinux.py
│   │   │   │   │   │   └── _parser.py
│   │   │   │   │   │   └── _structures.py
│   │   │   │   │   │   └── _tokenizer.py
│   │   │   │   │   │   ├── licenses/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _spdx.cpython-313.pyc
│   │   │   │   │   │   │   └── _spdx.py
│   │   │   │   │   │   └── markers.py
│   │   │   │   │   │   └── metadata.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   │   └── requirements.py
│   │   │   │   │   │   └── specifiers.py
│   │   │   │   │   │   └── tags.py
│   │   │   │   │   │   └── utils.py
│   │   │   │   │   │   └── version.py
│   │   │   │   │   ├── pkg_resources/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   ├── platformdirs/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── __main__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   │   │   └── android.cpython-313.pyc
│   │   │   │   │   │   │   └── api.cpython-313.pyc
│   │   │   │   │   │   │   └── macos.cpython-313.pyc
│   │   │   │   │   │   │   └── unix.cpython-313.pyc
│   │   │   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   │   │   │   └── windows.cpython-313.pyc
│   │   │   │   │   │   └── android.py
│   │   │   │   │   │   └── api.py
│   │   │   │   │   │   └── macos.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   │   └── unix.py
│   │   │   │   │   │   └── version.py
│   │   │   │   │   │   └── windows.py
│   │   │   │   │   ├── pygments/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── __main__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   │   │   └── cmdline.cpython-313.pyc
│   │   │   │   │   │   │   └── console.cpython-313.pyc
│   │   │   │   │   │   │   └── filter.cpython-313.pyc
│   │   │   │   │   │   │   └── formatter.cpython-313.pyc
│   │   │   │   │   │   │   └── lexer.cpython-313.pyc
│   │   │   │   │   │   │   └── modeline.cpython-313.pyc
│   │   │   │   │   │   │   └── plugin.cpython-313.pyc
│   │   │   │   │   │   │   └── regexopt.cpython-313.pyc
│   │   │   │   │   │   │   └── scanner.cpython-313.pyc
│   │   │   │   │   │   │   └── sphinxext.cpython-313.pyc
│   │   │   │   │   │   │   └── style.cpython-313.pyc
│   │   │   │   │   │   │   └── token.cpython-313.pyc
│   │   │   │   │   │   │   └── unistring.cpython-313.pyc
│   │   │   │   │   │   │   └── util.cpython-313.pyc
│   │   │   │   │   │   └── cmdline.py
│   │   │   │   │   │   └── console.py
│   │   │   │   │   │   └── filter.py
│   │   │   │   │   │   ├── filters/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── formatter.py
│   │   │   │   │   │   ├── formatters/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _mapping.cpython-313.pyc
│   │   │   │   │   │   │   │   └── bbcode.cpython-313.pyc
│   │   │   │   │   │   │   │   └── groff.cpython-313.pyc
│   │   │   │   │   │   │   │   └── html.cpython-313.pyc
│   │   │   │   │   │   │   │   └── img.cpython-313.pyc
│   │   │   │   │   │   │   │   └── irc.cpython-313.pyc
│   │   │   │   │   │   │   │   └── latex.cpython-313.pyc
│   │   │   │   │   │   │   │   └── other.cpython-313.pyc
│   │   │   │   │   │   │   │   └── pangomarkup.cpython-313.pyc
│   │   │   │   │   │   │   │   └── rtf.cpython-313.pyc
│   │   │   │   │   │   │   │   └── svg.cpython-313.pyc
│   │   │   │   │   │   │   │   └── terminal.cpython-313.pyc
│   │   │   │   │   │   │   │   └── terminal256.cpython-313.pyc
│   │   │   │   │   │   │   └── _mapping.py
│   │   │   │   │   │   │   └── bbcode.py
│   │   │   │   │   │   │   └── groff.py
│   │   │   │   │   │   │   └── html.py
│   │   │   │   │   │   │   └── img.py
│   │   │   │   │   │   │   └── irc.py
│   │   │   │   │   │   │   └── latex.py
│   │   │   │   │   │   │   └── other.py
│   │   │   │   │   │   │   └── pangomarkup.py
│   │   │   │   │   │   │   └── rtf.py
│   │   │   │   │   │   │   └── svg.py
│   │   │   │   │   │   │   └── terminal.py
│   │   │   │   │   │   │   └── terminal256.py
│   │   │   │   │   │   └── lexer.py
│   │   │   │   │   │   ├── lexers/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _mapping.cpython-313.pyc
│   │   │   │   │   │   │   │   └── python.cpython-313.pyc
│   │   │   │   │   │   │   └── _mapping.py
│   │   │   │   │   │   │   └── python.py
│   │   │   │   │   │   └── modeline.py
│   │   │   │   │   │   └── plugin.py
│   │   │   │   │   │   └── regexopt.py
│   │   │   │   │   │   └── scanner.py
│   │   │   │   │   │   └── sphinxext.py
│   │   │   │   │   │   └── style.py
│   │   │   │   │   │   ├── styles/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _mapping.cpython-313.pyc
│   │   │   │   │   │   │   └── _mapping.py
│   │   │   │   │   │   └── token.py
│   │   │   │   │   │   └── unistring.py
│   │   │   │   │   │   └── util.py
│   │   │   │   │   ├── pyproject_hooks/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _impl.cpython-313.pyc
│   │   │   │   │   │   └── _impl.py
│   │   │   │   │   │   ├── _in_process/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _in_process.cpython-313.pyc
│   │   │   │   │   │   │   └── _in_process.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   ├── requests/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── __version__.cpython-313.pyc
│   │   │   │   │   │   │   └── _internal_utils.cpython-313.pyc
│   │   │   │   │   │   │   └── adapters.cpython-313.pyc
│   │   │   │   │   │   │   └── api.cpython-313.pyc
│   │   │   │   │   │   │   └── auth.cpython-313.pyc
│   │   │   │   │   │   │   └── certs.cpython-313.pyc
│   │   │   │   │   │   │   └── compat.cpython-313.pyc
│   │   │   │   │   │   │   └── cookies.cpython-313.pyc
│   │   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   │   └── help.cpython-313.pyc
│   │   │   │   │   │   │   └── hooks.cpython-313.pyc
│   │   │   │   │   │   │   └── models.cpython-313.pyc
│   │   │   │   │   │   │   └── packages.cpython-313.pyc
│   │   │   │   │   │   │   └── sessions.cpython-313.pyc
│   │   │   │   │   │   │   └── status_codes.cpython-313.pyc
│   │   │   │   │   │   │   └── structures.cpython-313.pyc
│   │   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   └── __version__.py
│   │   │   │   │   │   └── _internal_utils.py
│   │   │   │   │   │   └── adapters.py
│   │   │   │   │   │   └── api.py
│   │   │   │   │   │   └── auth.py
│   │   │   │   │   │   └── certs.py
│   │   │   │   │   │   └── compat.py
│   │   │   │   │   │   └── cookies.py
│   │   │   │   │   │   └── exceptions.py
│   │   │   │   │   │   └── help.py
│   │   │   │   │   │   └── hooks.py
│   │   │   │   │   │   └── models.py
│   │   │   │   │   │   └── packages.py
│   │   │   │   │   │   └── sessions.py
│   │   │   │   │   │   └── status_codes.py
│   │   │   │   │   │   └── structures.py
│   │   │   │   │   │   └── utils.py
│   │   │   │   │   ├── resolvelib/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── providers.cpython-313.pyc
│   │   │   │   │   │   │   └── reporters.cpython-313.pyc
│   │   │   │   │   │   │   └── resolvers.cpython-313.pyc
│   │   │   │   │   │   │   └── structs.cpython-313.pyc
│   │   │   │   │   │   ├── compat/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── collections_abc.cpython-313.pyc
│   │   │   │   │   │   │   └── collections_abc.py
│   │   │   │   │   │   └── providers.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   │   └── reporters.py
│   │   │   │   │   │   └── resolvers.py
│   │   │   │   │   │   └── structs.py
│   │   │   │   │   ├── rich/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── __main__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   │   │   └── _cell_widths.cpython-313.pyc
│   │   │   │   │   │   │   └── _emoji_codes.cpython-313.pyc
│   │   │   │   │   │   │   └── _emoji_replace.cpython-313.pyc
│   │   │   │   │   │   │   └── _export_format.cpython-313.pyc
│   │   │   │   │   │   │   └── _extension.cpython-313.pyc
│   │   │   │   │   │   │   └── _fileno.cpython-313.pyc
│   │   │   │   │   │   │   └── _inspect.cpython-313.pyc
│   │   │   │   │   │   │   └── _log_render.cpython-313.pyc
│   │   │   │   │   │   │   └── _loop.cpython-313.pyc
│   │   │   │   │   │   │   └── _null_file.cpython-313.pyc
│   │   │   │   │   │   │   └── _palettes.cpython-313.pyc
│   │   │   │   │   │   │   └── _pick.cpython-313.pyc
│   │   │   │   │   │   │   └── _ratio.cpython-313.pyc
│   │   │   │   │   │   │   └── _spinners.cpython-313.pyc
│   │   │   │   │   │   │   └── _stack.cpython-313.pyc
│   │   │   │   │   │   │   └── _timer.cpython-313.pyc
│   │   │   │   │   │   │   └── _win32_console.cpython-313.pyc
│   │   │   │   │   │   │   └── _windows.cpython-313.pyc
│   │   │   │   │   │   │   └── _windows_renderer.cpython-313.pyc
│   │   │   │   │   │   │   └── _wrap.cpython-313.pyc
│   │   │   │   │   │   │   └── abc.cpython-313.pyc
│   │   │   │   │   │   │   └── align.cpython-313.pyc
│   │   │   │   │   │   │   └── ansi.cpython-313.pyc
│   │   │   │   │   │   │   └── bar.cpython-313.pyc
│   │   │   │   │   │   │   └── box.cpython-313.pyc
│   │   │   │   │   │   │   └── cells.cpython-313.pyc
│   │   │   │   │   │   │   └── color.cpython-313.pyc
│   │   │   │   │   │   │   └── color_triplet.cpython-313.pyc
│   │   │   │   │   │   │   └── columns.cpython-313.pyc
│   │   │   │   │   │   │   └── console.cpython-313.pyc
│   │   │   │   │   │   │   └── constrain.cpython-313.pyc
│   │   │   │   │   │   │   └── containers.cpython-313.pyc
│   │   │   │   │   │   │   └── control.cpython-313.pyc
│   │   │   │   │   │   │   └── default_styles.cpython-313.pyc
│   │   │   │   │   │   │   └── diagnose.cpython-313.pyc
│   │   │   │   │   │   │   └── emoji.cpython-313.pyc
│   │   │   │   │   │   │   └── errors.cpython-313.pyc
│   │   │   │   │   │   │   └── file_proxy.cpython-313.pyc
│   │   │   │   │   │   │   └── filesize.cpython-313.pyc
│   │   │   │   │   │   │   └── highlighter.cpython-313.pyc
│   │   │   │   │   │   │   └── json.cpython-313.pyc
│   │   │   │   │   │   │   └── jupyter.cpython-313.pyc
│   │   │   │   │   │   │   └── layout.cpython-313.pyc
│   │   │   │   │   │   │   └── live.cpython-313.pyc
│   │   │   │   │   │   │   └── live_render.cpython-313.pyc
│   │   │   │   │   │   │   └── logging.cpython-313.pyc
│   │   │   │   │   │   │   └── markup.cpython-313.pyc
│   │   │   │   │   │   │   └── measure.cpython-313.pyc
│   │   │   │   │   │   │   └── padding.cpython-313.pyc
│   │   │   │   │   │   │   └── pager.cpython-313.pyc
│   │   │   │   │   │   │   └── palette.cpython-313.pyc
│   │   │   │   │   │   │   └── panel.cpython-313.pyc
│   │   │   │   │   │   │   └── pretty.cpython-313.pyc
│   │   │   │   │   │   │   └── progress.cpython-313.pyc
│   │   │   │   │   │   │   └── progress_bar.cpython-313.pyc
│   │   │   │   │   │   │   └── prompt.cpython-313.pyc
│   │   │   │   │   │   │   └── protocol.cpython-313.pyc
│   │   │   │   │   │   │   └── region.cpython-313.pyc
│   │   │   │   │   │   │   └── repr.cpython-313.pyc
│   │   │   │   │   │   │   └── rule.cpython-313.pyc
│   │   │   │   │   │   │   └── scope.cpython-313.pyc
│   │   │   │   │   │   │   └── screen.cpython-313.pyc
│   │   │   │   │   │   │   └── segment.cpython-313.pyc
│   │   │   │   │   │   │   └── spinner.cpython-313.pyc
│   │   │   │   │   │   │   └── status.cpython-313.pyc
│   │   │   │   │   │   │   └── style.cpython-313.pyc
│   │   │   │   │   │   │   └── styled.cpython-313.pyc
│   │   │   │   │   │   │   └── syntax.cpython-313.pyc
│   │   │   │   │   │   │   └── table.cpython-313.pyc
│   │   │   │   │   │   │   └── terminal_theme.cpython-313.pyc
│   │   │   │   │   │   │   └── text.cpython-313.pyc
│   │   │   │   │   │   │   └── theme.cpython-313.pyc
│   │   │   │   │   │   │   └── themes.cpython-313.pyc
│   │   │   │   │   │   │   └── traceback.cpython-313.pyc
│   │   │   │   │   │   │   └── tree.cpython-313.pyc
│   │   │   │   │   │   └── _cell_widths.py
│   │   │   │   │   │   └── _emoji_codes.py
│   │   │   │   │   │   └── _emoji_replace.py
│   │   │   │   │   │   └── _export_format.py
│   │   │   │   │   │   └── _extension.py
│   │   │   │   │   │   └── _fileno.py
│   │   │   │   │   │   └── _inspect.py
│   │   │   │   │   │   └── _log_render.py
│   │   │   │   │   │   └── _loop.py
│   │   │   │   │   │   └── _null_file.py
│   │   │   │   │   │   └── _palettes.py
│   │   │   │   │   │   └── _pick.py
│   │   │   │   │   │   └── _ratio.py
│   │   │   │   │   │   └── _spinners.py
│   │   │   │   │   │   └── _stack.py
│   │   │   │   │   │   └── _timer.py
│   │   │   │   │   │   └── _win32_console.py
│   │   │   │   │   │   └── _windows.py
│   │   │   │   │   │   └── _windows_renderer.py
│   │   │   │   │   │   └── _wrap.py
│   │   │   │   │   │   └── abc.py
│   │   │   │   │   │   └── align.py
│   │   │   │   │   │   └── ansi.py
│   │   │   │   │   │   └── bar.py
│   │   │   │   │   │   └── box.py
│   │   │   │   │   │   └── cells.py
│   │   │   │   │   │   └── color.py
│   │   │   │   │   │   └── color_triplet.py
│   │   │   │   │   │   └── columns.py
│   │   │   │   │   │   └── console.py
│   │   │   │   │   │   └── constrain.py
│   │   │   │   │   │   └── containers.py
│   │   │   │   │   │   └── control.py
│   │   │   │   │   │   └── default_styles.py
│   │   │   │   │   │   └── diagnose.py
│   │   │   │   │   │   └── emoji.py
│   │   │   │   │   │   └── errors.py
│   │   │   │   │   │   └── file_proxy.py
│   │   │   │   │   │   └── filesize.py
│   │   │   │   │   │   └── highlighter.py
│   │   │   │   │   │   └── json.py
│   │   │   │   │   │   └── jupyter.py
│   │   │   │   │   │   └── layout.py
│   │   │   │   │   │   └── live.py
│   │   │   │   │   │   └── live_render.py
│   │   │   │   │   │   └── logging.py
│   │   │   │   │   │   └── markup.py
│   │   │   │   │   │   └── measure.py
│   │   │   │   │   │   └── padding.py
│   │   │   │   │   │   └── pager.py
│   │   │   │   │   │   └── palette.py
│   │   │   │   │   │   └── panel.py
│   │   │   │   │   │   └── pretty.py
│   │   │   │   │   │   └── progress.py
│   │   │   │   │   │   └── progress_bar.py
│   │   │   │   │   │   └── prompt.py
│   │   │   │   │   │   └── protocol.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   │   └── region.py
│   │   │   │   │   │   └── repr.py
│   │   │   │   │   │   └── rule.py
│   │   │   │   │   │   └── scope.py
│   │   │   │   │   │   └── screen.py
│   │   │   │   │   │   └── segment.py
│   │   │   │   │   │   └── spinner.py
│   │   │   │   │   │   └── status.py
│   │   │   │   │   │   └── style.py
│   │   │   │   │   │   └── styled.py
│   │   │   │   │   │   └── syntax.py
│   │   │   │   │   │   └── table.py
│   │   │   │   │   │   └── terminal_theme.py
│   │   │   │   │   │   └── text.py
│   │   │   │   │   │   └── theme.py
│   │   │   │   │   │   └── themes.py
│   │   │   │   │   │   └── traceback.py
│   │   │   │   │   │   └── tree.py
│   │   │   │   │   ├── tomli/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _parser.cpython-313.pyc
│   │   │   │   │   │   │   └── _re.cpython-313.pyc
│   │   │   │   │   │   │   └── _types.cpython-313.pyc
│   │   │   │   │   │   └── _parser.py
│   │   │   │   │   │   └── _re.py
│   │   │   │   │   │   └── _types.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   ├── truststore/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _api.cpython-313.pyc
│   │   │   │   │   │   │   └── _macos.cpython-313.pyc
│   │   │   │   │   │   │   └── _openssl.cpython-313.pyc
│   │   │   │   │   │   │   └── _ssl_constants.cpython-313.pyc
│   │   │   │   │   │   │   └── _windows.cpython-313.pyc
│   │   │   │   │   │   └── _api.py
│   │   │   │   │   │   └── _macos.py
│   │   │   │   │   │   └── _openssl.py
│   │   │   │   │   │   └── _ssl_constants.py
│   │   │   │   │   │   └── _windows.py
│   │   │   │   │   │   └── py.typed
│   │   │   │   │   └── typing_extensions.py
│   │   │   │   │   ├── urllib3/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── _collections.cpython-313.pyc
│   │   │   │   │   │   │   └── _version.cpython-313.pyc
│   │   │   │   │   │   │   └── connection.cpython-313.pyc
│   │   │   │   │   │   │   └── connectionpool.cpython-313.pyc
│   │   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   │   └── fields.cpython-313.pyc
│   │   │   │   │   │   │   └── filepost.cpython-313.pyc
│   │   │   │   │   │   │   └── poolmanager.cpython-313.pyc
│   │   │   │   │   │   │   └── request.cpython-313.pyc
│   │   │   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   │   │   └── _collections.py
│   │   │   │   │   │   └── _version.py
│   │   │   │   │   │   └── connection.py
│   │   │   │   │   │   └── connectionpool.py
│   │   │   │   │   │   ├── contrib/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── _appengine_environ.cpython-313.pyc
│   │   │   │   │   │   │   │   └── appengine.cpython-313.pyc
│   │   │   │   │   │   │   │   └── ntlmpool.cpython-313.pyc
│   │   │   │   │   │   │   │   └── pyopenssl.cpython-313.pyc
│   │   │   │   │   │   │   │   └── securetransport.cpython-313.pyc
│   │   │   │   │   │   │   │   └── socks.cpython-313.pyc
│   │   │   │   │   │   │   └── _appengine_environ.py
│   │   │   │   │   │   │   ├── _securetransport/
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── bindings.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── low_level.cpython-313.pyc
│   │   │   │   │   │   │   │   └── bindings.py
│   │   │   │   │   │   │   │   └── low_level.py
│   │   │   │   │   │   │   └── appengine.py
│   │   │   │   │   │   │   └── ntlmpool.py
│   │   │   │   │   │   │   └── pyopenssl.py
│   │   │   │   │   │   │   └── securetransport.py
│   │   │   │   │   │   │   └── socks.py
│   │   │   │   │   │   └── exceptions.py
│   │   │   │   │   │   └── fields.py
│   │   │   │   │   │   └── filepost.py
│   │   │   │   │   │   ├── packages/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── six.cpython-313.pyc
│   │   │   │   │   │   │   ├── backports/
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── makefile.cpython-313.pyc
│   │   │   │   │   │   │   │   │   └── weakref_finalize.cpython-313.pyc
│   │   │   │   │   │   │   │   └── makefile.py
│   │   │   │   │   │   │   │   └── weakref_finalize.py
│   │   │   │   │   │   │   └── six.py
│   │   │   │   │   │   └── poolmanager.py
│   │   │   │   │   │   └── request.py
│   │   │   │   │   │   └── response.py
│   │   │   │   │   │   ├── util/
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   │   └── connection.cpython-313.pyc
│   │   │   │   │   │   │   │   └── proxy.cpython-313.pyc
│   │   │   │   │   │   │   │   └── queue.cpython-313.pyc
│   │   │   │   │   │   │   │   └── request.cpython-313.pyc
│   │   │   │   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   │   │   │   │   └── retry.cpython-313.pyc
│   │   │   │   │   │   │   │   └── ssl_.cpython-313.pyc
│   │   │   │   │   │   │   │   └── ssl_match_hostname.cpython-313.pyc
│   │   │   │   │   │   │   │   └── ssltransport.cpython-313.pyc
│   │   │   │   │   │   │   │   └── timeout.cpython-313.pyc
│   │   │   │   │   │   │   │   └── url.cpython-313.pyc
│   │   │   │   │   │   │   │   └── wait.cpython-313.pyc
│   │   │   │   │   │   │   └── connection.py
│   │   │   │   │   │   │   └── proxy.py
│   │   │   │   │   │   │   └── queue.py
│   │   │   │   │   │   │   └── request.py
│   │   │   │   │   │   │   └── response.py
│   │   │   │   │   │   │   └── retry.py
│   │   │   │   │   │   │   └── ssl_.py
│   │   │   │   │   │   │   └── ssl_match_hostname.py
│   │   │   │   │   │   │   └── ssltransport.py
│   │   │   │   │   │   │   └── timeout.py
│   │   │   │   │   │   │   └── url.py
│   │   │   │   │   │   │   └── wait.py
│   │   │   │   │   └── vendor.txt
│   │   │   │   └── py.typed
│   │   │   ├── pip-25.0.1.dist-info/
│   │   │   │   └── AUTHORS.txt
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   │   └── top_level.txt
│   │   │   ├── platformdirs/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── android.cpython-313.pyc
│   │   │   │   │   └── api.cpython-313.pyc
│   │   │   │   │   └── macos.cpython-313.pyc
│   │   │   │   │   └── unix.cpython-313.pyc
│   │   │   │   │   └── version.cpython-313.pyc
│   │   │   │   │   └── windows.cpython-313.pyc
│   │   │   │   └── android.py
│   │   │   │   └── api.py
│   │   │   │   └── macos.py
│   │   │   │   └── py.typed
│   │   │   │   └── unix.py
│   │   │   │   └── version.py
│   │   │   │   └── windows.py
│   │   │   ├── platformdirs-4.3.7.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE
│   │   │   ├── python_dotenv-1.1.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── entry_points.txt
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE
│   │   │   │   └── top_level.txt
│   │   │   ├── pytz/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── lazy.cpython-313.pyc
│   │   │   │   │   └── reference.cpython-313.pyc
│   │   │   │   │   └── tzfile.cpython-313.pyc
│   │   │   │   │   └── tzinfo.cpython-313.pyc
│   │   │   │   └── exceptions.py
│   │   │   │   └── lazy.py
│   │   │   │   └── reference.py
│   │   │   │   └── tzfile.py
│   │   │   │   └── tzinfo.py
│   │   │   │   ├── zoneinfo/
│   │   │   │   │   ├── Africa/
│   │   │   │   │   │   └── Abidjan
│   │   │   │   │   │   └── Accra
│   │   │   │   │   │   └── Addis_Ababa
│   │   │   │   │   │   └── Algiers
│   │   │   │   │   │   └── Asmara
│   │   │   │   │   │   └── Asmera
│   │   │   │   │   │   └── Bamako
│   │   │   │   │   │   └── Bangui
│   │   │   │   │   │   └── Banjul
│   │   │   │   │   │   └── Bissau
│   │   │   │   │   │   └── Blantyre
│   │   │   │   │   │   └── Brazzaville
│   │   │   │   │   │   └── Bujumbura
│   │   │   │   │   │   └── Cairo
│   │   │   │   │   │   └── Casablanca
│   │   │   │   │   │   └── Ceuta
│   │   │   │   │   │   └── Conakry
│   │   │   │   │   │   └── Dakar
│   │   │   │   │   │   └── Dar_es_Salaam
│   │   │   │   │   │   └── Djibouti
│   │   │   │   │   │   └── Douala
│   │   │   │   │   │   └── El_Aaiun
│   │   │   │   │   │   └── Freetown
│   │   │   │   │   │   └── Gaborone
│   │   │   │   │   │   └── Harare
│   │   │   │   │   │   └── Johannesburg
│   │   │   │   │   │   └── Juba
│   │   │   │   │   │   └── Kampala
│   │   │   │   │   │   └── Khartoum
│   │   │   │   │   │   └── Kigali
│   │   │   │   │   │   └── Kinshasa
│   │   │   │   │   │   └── Lagos
│   │   │   │   │   │   └── Libreville
│   │   │   │   │   │   └── Lome
│   │   │   │   │   │   └── Luanda
│   │   │   │   │   │   └── Lubumbashi
│   │   │   │   │   │   └── Lusaka
│   │   │   │   │   │   └── Malabo
│   │   │   │   │   │   └── Maputo
│   │   │   │   │   │   └── Maseru
│   │   │   │   │   │   └── Mbabane
│   │   │   │   │   │   └── Mogadishu
│   │   │   │   │   │   └── Monrovia
│   │   │   │   │   │   └── Nairobi
│   │   │   │   │   │   └── Ndjamena
│   │   │   │   │   │   └── Niamey
│   │   │   │   │   │   └── Nouakchott
│   │   │   │   │   │   └── Ouagadougou
│   │   │   │   │   │   └── Porto-Novo
│   │   │   │   │   │   └── Sao_Tome
│   │   │   │   │   │   └── Timbuktu
│   │   │   │   │   │   └── Tripoli
│   │   │   │   │   │   └── Tunis
│   │   │   │   │   │   └── Windhoek
│   │   │   │   │   ├── America/
│   │   │   │   │   │   └── Adak
│   │   │   │   │   │   └── Anchorage
│   │   │   │   │   │   └── Anguilla
│   │   │   │   │   │   └── Antigua
│   │   │   │   │   │   └── Araguaina
│   │   │   │   │   │   ├── Argentina/
│   │   │   │   │   │   │   └── Buenos_Aires
│   │   │   │   │   │   │   └── Catamarca
│   │   │   │   │   │   │   └── ComodRivadavia
│   │   │   │   │   │   │   └── Cordoba
│   │   │   │   │   │   │   └── Jujuy
│   │   │   │   │   │   │   └── La_Rioja
│   │   │   │   │   │   │   └── Mendoza
│   │   │   │   │   │   │   └── Rio_Gallegos
│   │   │   │   │   │   │   └── Salta
│   │   │   │   │   │   │   └── San_Juan
│   │   │   │   │   │   │   └── San_Luis
│   │   │   │   │   │   │   └── Tucuman
│   │   │   │   │   │   │   └── Ushuaia
│   │   │   │   │   │   └── Aruba
│   │   │   │   │   │   └── Asuncion
│   │   │   │   │   │   └── Atikokan
│   │   │   │   │   │   └── Atka
│   │   │   │   │   │   └── Bahia
│   │   │   │   │   │   └── Bahia_Banderas
│   │   │   │   │   │   └── Barbados
│   │   │   │   │   │   └── Belem
│   │   │   │   │   │   └── Belize
│   │   │   │   │   │   └── Blanc-Sablon
│   │   │   │   │   │   └── Boa_Vista
│   │   │   │   │   │   └── Bogota
│   │   │   │   │   │   └── Boise
│   │   │   │   │   │   └── Buenos_Aires
│   │   │   │   │   │   └── Cambridge_Bay
│   │   │   │   │   │   └── Campo_Grande
│   │   │   │   │   │   └── Cancun
│   │   │   │   │   │   └── Caracas
│   │   │   │   │   │   └── Catamarca
│   │   │   │   │   │   └── Cayenne
│   │   │   │   │   │   └── Cayman
│   │   │   │   │   │   └── Chicago
│   │   │   │   │   │   └── Chihuahua
│   │   │   │   │   │   └── Ciudad_Juarez
│   │   │   │   │   │   └── Coral_Harbour
│   │   │   │   │   │   └── Cordoba
│   │   │   │   │   │   └── Costa_Rica
│   │   │   │   │   │   └── Coyhaique
│   │   │   │   │   │   └── Creston
│   │   │   │   │   │   └── Cuiaba
│   │   │   │   │   │   └── Curacao
│   │   │   │   │   │   └── Danmarkshavn
│   │   │   │   │   │   └── Dawson
│   │   │   │   │   │   └── Dawson_Creek
│   │   │   │   │   │   └── Denver
│   │   │   │   │   │   └── Detroit
│   │   │   │   │   │   └── Dominica
│   │   │   │   │   │   └── Edmonton
│   │   │   │   │   │   └── Eirunepe
│   │   │   │   │   │   └── El_Salvador
│   │   │   │   │   │   └── Ensenada
│   │   │   │   │   │   └── Fort_Nelson
│   │   │   │   │   │   └── Fort_Wayne
│   │   │   │   │   │   └── Fortaleza
│   │   │   │   │   │   └── Glace_Bay
│   │   │   │   │   │   └── Godthab
│   │   │   │   │   │   └── Goose_Bay
│   │   │   │   │   │   └── Grand_Turk
│   │   │   │   │   │   └── Grenada
│   │   │   │   │   │   └── Guadeloupe
│   │   │   │   │   │   └── Guatemala
│   │   │   │   │   │   └── Guayaquil
│   │   │   │   │   │   └── Guyana
│   │   │   │   │   │   └── Halifax
│   │   │   │   │   │   └── Havana
│   │   │   │   │   │   └── Hermosillo
│   │   │   │   │   │   ├── Indiana/
│   │   │   │   │   │   │   └── Indianapolis
│   │   │   │   │   │   │   └── Knox
│   │   │   │   │   │   │   └── Marengo
│   │   │   │   │   │   │   └── Petersburg
│   │   │   │   │   │   │   └── Tell_City
│   │   │   │   │   │   │   └── Vevay
│   │   │   │   │   │   │   └── Vincennes
│   │   │   │   │   │   │   └── Winamac
│   │   │   │   │   │   └── Indianapolis
│   │   │   │   │   │   └── Inuvik
│   │   │   │   │   │   └── Iqaluit
│   │   │   │   │   │   └── Jamaica
│   │   │   │   │   │   └── Jujuy
│   │   │   │   │   │   └── Juneau
│   │   │   │   │   │   ├── Kentucky/
│   │   │   │   │   │   │   └── Louisville
│   │   │   │   │   │   │   └── Monticello
│   │   │   │   │   │   └── Knox_IN
│   │   │   │   │   │   └── Kralendijk
│   │   │   │   │   │   └── La_Paz
│   │   │   │   │   │   └── Lima
│   │   │   │   │   │   └── Los_Angeles
│   │   │   │   │   │   └── Louisville
│   │   │   │   │   │   └── Lower_Princes
│   │   │   │   │   │   └── Maceio
│   │   │   │   │   │   └── Managua
│   │   │   │   │   │   └── Manaus
│   │   │   │   │   │   └── Marigot
│   │   │   │   │   │   └── Martinique
│   │   │   │   │   │   └── Matamoros
│   │   │   │   │   │   └── Mazatlan
│   │   │   │   │   │   └── Mendoza
│   │   │   │   │   │   └── Menominee
│   │   │   │   │   │   └── Merida
│   │   │   │   │   │   └── Metlakatla
│   │   │   │   │   │   └── Mexico_City
│   │   │   │   │   │   └── Miquelon
│   │   │   │   │   │   └── Moncton
│   │   │   │   │   │   └── Monterrey
│   │   │   │   │   │   └── Montevideo
│   │   │   │   │   │   └── Montreal
│   │   │   │   │   │   └── Montserrat
│   │   │   │   │   │   └── Nassau
│   │   │   │   │   │   └── New_York
│   │   │   │   │   │   └── Nipigon
│   │   │   │   │   │   └── Nome
│   │   │   │   │   │   └── Noronha
│   │   │   │   │   │   ├── North_Dakota/
│   │   │   │   │   │   │   └── Beulah
│   │   │   │   │   │   │   └── Center
│   │   │   │   │   │   │   └── New_Salem
│   │   │   │   │   │   └── Nuuk
│   │   │   │   │   │   └── Ojinaga
│   │   │   │   │   │   └── Panama
│   │   │   │   │   │   └── Pangnirtung
│   │   │   │   │   │   └── Paramaribo
│   │   │   │   │   │   └── Phoenix
│   │   │   │   │   │   └── Port-au-Prince
│   │   │   │   │   │   └── Port_of_Spain
│   │   │   │   │   │   └── Porto_Acre
│   │   │   │   │   │   └── Porto_Velho
│   │   │   │   │   │   └── Puerto_Rico
│   │   │   │   │   │   └── Punta_Arenas
│   │   │   │   │   │   └── Rainy_River
│   │   │   │   │   │   └── Rankin_Inlet
│   │   │   │   │   │   └── Recife
│   │   │   │   │   │   └── Regina
│   │   │   │   │   │   └── Resolute
│   │   │   │   │   │   └── Rio_Branco
│   │   │   │   │   │   └── Rosario
│   │   │   │   │   │   └── Santa_Isabel
│   │   │   │   │   │   └── Santarem
│   │   │   │   │   │   └── Santiago
│   │   │   │   │   │   └── Santo_Domingo
│   │   │   │   │   │   └── Sao_Paulo
│   │   │   │   │   │   └── Scoresbysund
│   │   │   │   │   │   └── Shiprock
│   │   │   │   │   │   └── Sitka
│   │   │   │   │   │   └── St_Barthelemy
│   │   │   │   │   │   └── St_Johns
│   │   │   │   │   │   └── St_Kitts
│   │   │   │   │   │   └── St_Lucia
│   │   │   │   │   │   └── St_Thomas
│   │   │   │   │   │   └── St_Vincent
│   │   │   │   │   │   └── Swift_Current
│   │   │   │   │   │   └── Tegucigalpa
│   │   │   │   │   │   └── Thule
│   │   │   │   │   │   └── Thunder_Bay
│   │   │   │   │   │   └── Tijuana
│   │   │   │   │   │   └── Toronto
│   │   │   │   │   │   └── Tortola
│   │   │   │   │   │   └── Vancouver
│   │   │   │   │   │   └── Virgin
│   │   │   │   │   │   └── Whitehorse
│   │   │   │   │   │   └── Winnipeg
│   │   │   │   │   │   └── Yakutat
│   │   │   │   │   │   └── Yellowknife
│   │   │   │   │   ├── Antarctica/
│   │   │   │   │   │   └── Casey
│   │   │   │   │   │   └── Davis
│   │   │   │   │   │   └── DumontDUrville
│   │   │   │   │   │   └── Macquarie
│   │   │   │   │   │   └── Mawson
│   │   │   │   │   │   └── McMurdo
│   │   │   │   │   │   └── Palmer
│   │   │   │   │   │   └── Rothera
│   │   │   │   │   │   └── South_Pole
│   │   │   │   │   │   └── Syowa
│   │   │   │   │   │   └── Troll
│   │   │   │   │   │   └── Vostok
│   │   │   │   │   ├── Arctic/
│   │   │   │   │   │   └── Longyearbyen
│   │   │   │   │   ├── Asia/
│   │   │   │   │   │   └── Aden
│   │   │   │   │   │   └── Almaty
│   │   │   │   │   │   └── Amman
│   │   │   │   │   │   └── Anadyr
│   │   │   │   │   │   └── Aqtau
│   │   │   │   │   │   └── Aqtobe
│   │   │   │   │   │   └── Ashgabat
│   │   │   │   │   │   └── Ashkhabad
│   │   │   │   │   │   └── Atyrau
│   │   │   │   │   │   └── Baghdad
│   │   │   │   │   │   └── Bahrain
│   │   │   │   │   │   └── Baku
│   │   │   │   │   │   └── Bangkok
│   │   │   │   │   │   └── Barnaul
│   │   │   │   │   │   └── Beirut
│   │   │   │   │   │   └── Bishkek
│   │   │   │   │   │   └── Brunei
│   │   │   │   │   │   └── Calcutta
│   │   │   │   │   │   └── Chita
│   │   │   │   │   │   └── Choibalsan
│   │   │   │   │   │   └── Chongqing
│   │   │   │   │   │   └── Chungking
│   │   │   │   │   │   └── Colombo
│   │   │   │   │   │   └── Dacca
│   │   │   │   │   │   └── Damascus
│   │   │   │   │   │   └── Dhaka
│   │   │   │   │   │   └── Dili
│   │   │   │   │   │   └── Dubai
│   │   │   │   │   │   └── Dushanbe
│   │   │   │   │   │   └── Famagusta
│   │   │   │   │   │   └── Gaza
│   │   │   │   │   │   └── Harbin
│   │   │   │   │   │   └── Hebron
│   │   │   │   │   │   └── Ho_Chi_Minh
│   │   │   │   │   │   └── Hong_Kong
│   │   │   │   │   │   └── Hovd
│   │   │   │   │   │   └── Irkutsk
│   │   │   │   │   │   └── Istanbul
│   │   │   │   │   │   └── Jakarta
│   │   │   │   │   │   └── Jayapura
│   │   │   │   │   │   └── Jerusalem
│   │   │   │   │   │   └── Kabul
│   │   │   │   │   │   └── Kamchatka
│   │   │   │   │   │   └── Karachi
│   │   │   │   │   │   └── Kashgar
│   │   │   │   │   │   └── Kathmandu
│   │   │   │   │   │   └── Katmandu
│   │   │   │   │   │   └── Khandyga
│   │   │   │   │   │   └── Kolkata
│   │   │   │   │   │   └── Krasnoyarsk
│   │   │   │   │   │   └── Kuala_Lumpur
│   │   │   │   │   │   └── Kuching
│   │   │   │   │   │   └── Kuwait
│   │   │   │   │   │   └── Macao
│   │   │   │   │   │   └── Macau
│   │   │   │   │   │   └── Magadan
│   │   │   │   │   │   └── Makassar
│   │   │   │   │   │   └── Manila
│   │   │   │   │   │   └── Muscat
│   │   │   │   │   │   └── Nicosia
│   │   │   │   │   │   └── Novokuznetsk
│   │   │   │   │   │   └── Novosibirsk
│   │   │   │   │   │   └── Omsk
│   │   │   │   │   │   └── Oral
│   │   │   │   │   │   └── Phnom_Penh
│   │   │   │   │   │   └── Pontianak
│   │   │   │   │   │   └── Pyongyang
│   │   │   │   │   │   └── Qatar
│   │   │   │   │   │   └── Qostanay
│   │   │   │   │   │   └── Qyzylorda
│   │   │   │   │   │   └── Rangoon
│   │   │   │   │   │   └── Riyadh
│   │   │   │   │   │   └── Saigon
│   │   │   │   │   │   └── Sakhalin
│   │   │   │   │   │   └── Samarkand
│   │   │   │   │   │   └── Seoul
│   │   │   │   │   │   └── Shanghai
│   │   │   │   │   │   └── Singapore
│   │   │   │   │   │   └── Srednekolymsk
│   │   │   │   │   │   └── Taipei
│   │   │   │   │   │   └── Tashkent
│   │   │   │   │   │   └── Tbilisi
│   │   │   │   │   │   └── Tehran
│   │   │   │   │   │   └── Tel_Aviv
│   │   │   │   │   │   └── Thimbu
│   │   │   │   │   │   └── Thimphu
│   │   │   │   │   │   └── Tokyo
│   │   │   │   │   │   └── Tomsk
│   │   │   │   │   │   └── Ujung_Pandang
│   │   │   │   │   │   └── Ulaanbaatar
│   │   │   │   │   │   └── Ulan_Bator
│   │   │   │   │   │   └── Urumqi
│   │   │   │   │   │   └── Ust-Nera
│   │   │   │   │   │   └── Vientiane
│   │   │   │   │   │   └── Vladivostok
│   │   │   │   │   │   └── Yakutsk
│   │   │   │   │   │   └── Yangon
│   │   │   │   │   │   └── Yekaterinburg
│   │   │   │   │   │   └── Yerevan
│   │   │   │   │   ├── Atlantic/
│   │   │   │   │   │   └── Azores
│   │   │   │   │   │   └── Bermuda
│   │   │   │   │   │   └── Canary
│   │   │   │   │   │   └── Cape_Verde
│   │   │   │   │   │   └── Faeroe
│   │   │   │   │   │   └── Faroe
│   │   │   │   │   │   └── Jan_Mayen
│   │   │   │   │   │   └── Madeira
│   │   │   │   │   │   └── Reykjavik
│   │   │   │   │   │   └── South_Georgia
│   │   │   │   │   │   └── St_Helena
│   │   │   │   │   │   └── Stanley
│   │   │   │   │   ├── Australia/
│   │   │   │   │   │   └── ACT
│   │   │   │   │   │   └── Adelaide
│   │   │   │   │   │   └── Brisbane
│   │   │   │   │   │   └── Broken_Hill
│   │   │   │   │   │   └── Canberra
│   │   │   │   │   │   └── Currie
│   │   │   │   │   │   └── Darwin
│   │   │   │   │   │   └── Eucla
│   │   │   │   │   │   └── Hobart
│   │   │   │   │   │   └── LHI
│   │   │   │   │   │   └── Lindeman
│   │   │   │   │   │   └── Lord_Howe
│   │   │   │   │   │   └── Melbourne
│   │   │   │   │   │   └── NSW
│   │   │   │   │   │   └── North
│   │   │   │   │   │   └── Perth
│   │   │   │   │   │   └── Queensland
│   │   │   │   │   │   └── South
│   │   │   │   │   │   └── Sydney
│   │   │   │   │   │   └── Tasmania
│   │   │   │   │   │   └── Victoria
│   │   │   │   │   │   └── West
│   │   │   │   │   │   └── Yancowinna
│   │   │   │   │   ├── Brazil/
│   │   │   │   │   │   └── Acre
│   │   │   │   │   │   └── DeNoronha
│   │   │   │   │   │   └── East
│   │   │   │   │   │   └── West
│   │   │   │   │   └── CET
│   │   │   │   │   └── CST6CDT
│   │   │   │   │   ├── Canada/
│   │   │   │   │   │   └── Atlantic
│   │   │   │   │   │   └── Central
│   │   │   │   │   │   └── Eastern
│   │   │   │   │   │   └── Mountain
│   │   │   │   │   │   └── Newfoundland
│   │   │   │   │   │   └── Pacific
│   │   │   │   │   │   └── Saskatchewan
│   │   │   │   │   │   └── Yukon
│   │   │   │   │   ├── Chile/
│   │   │   │   │   │   └── Continental
│   │   │   │   │   │   └── EasterIsland
│   │   │   │   │   └── Cuba
│   │   │   │   │   └── EET
│   │   │   │   │   └── EST
│   │   │   │   │   └── EST5EDT
│   │   │   │   │   └── Egypt
│   │   │   │   │   └── Eire
│   │   │   │   │   ├── Etc/
│   │   │   │   │   │   └── GMT
│   │   │   │   │   │   └── GMT+0
│   │   │   │   │   │   └── GMT+1
│   │   │   │   │   │   └── GMT+10
│   │   │   │   │   │   └── GMT+11
│   │   │   │   │   │   └── GMT+12
│   │   │   │   │   │   └── GMT+2
│   │   │   │   │   │   └── GMT+3
│   │   │   │   │   │   └── GMT+4
│   │   │   │   │   │   └── GMT+5
│   │   │   │   │   │   └── GMT+6
│   │   │   │   │   │   └── GMT+7
│   │   │   │   │   │   └── GMT+8
│   │   │   │   │   │   └── GMT+9
│   │   │   │   │   │   └── GMT-0
│   │   │   │   │   │   └── GMT-1
│   │   │   │   │   │   └── GMT-10
│   │   │   │   │   │   └── GMT-11
│   │   │   │   │   │   └── GMT-12
│   │   │   │   │   │   └── GMT-13
│   │   │   │   │   │   └── GMT-14
│   │   │   │   │   │   └── GMT-2
│   │   │   │   │   │   └── GMT-3
│   │   │   │   │   │   └── GMT-4
│   │   │   │   │   │   └── GMT-5
│   │   │   │   │   │   └── GMT-6
│   │   │   │   │   │   └── GMT-7
│   │   │   │   │   │   └── GMT-8
│   │   │   │   │   │   └── GMT-9
│   │   │   │   │   │   └── GMT0
│   │   │   │   │   │   └── Greenwich
│   │   │   │   │   │   └── UCT
│   │   │   │   │   │   └── UTC
│   │   │   │   │   │   └── Universal
│   │   │   │   │   │   └── Zulu
│   │   │   │   │   ├── Europe/
│   │   │   │   │   │   └── Amsterdam
│   │   │   │   │   │   └── Andorra
│   │   │   │   │   │   └── Astrakhan
│   │   │   │   │   │   └── Athens
│   │   │   │   │   │   └── Belfast
│   │   │   │   │   │   └── Belgrade
│   │   │   │   │   │   └── Berlin
│   │   │   │   │   │   └── Bratislava
│   │   │   │   │   │   └── Brussels
│   │   │   │   │   │   └── Bucharest
│   │   │   │   │   │   └── Budapest
│   │   │   │   │   │   └── Busingen
│   │   │   │   │   │   └── Chisinau
│   │   │   │   │   │   └── Copenhagen
│   │   │   │   │   │   └── Dublin
│   │   │   │   │   │   └── Gibraltar
│   │   │   │   │   │   └── Guernsey
│   │   │   │   │   │   └── Helsinki
│   │   │   │   │   │   └── Isle_of_Man
│   │   │   │   │   │   └── Istanbul
│   │   │   │   │   │   └── Jersey
│   │   │   │   │   │   └── Kaliningrad
│   │   │   │   │   │   └── Kiev
│   │   │   │   │   │   └── Kirov
│   │   │   │   │   │   └── Kyiv
│   │   │   │   │   │   └── Lisbon
│   │   │   │   │   │   └── Ljubljana
│   │   │   │   │   │   └── London
│   │   │   │   │   │   └── Luxembourg
│   │   │   │   │   │   └── Madrid
│   │   │   │   │   │   └── Malta
│   │   │   │   │   │   └── Mariehamn
│   │   │   │   │   │   └── Minsk
│   │   │   │   │   │   └── Monaco
│   │   │   │   │   │   └── Moscow
│   │   │   │   │   │   └── Nicosia
│   │   │   │   │   │   └── Oslo
│   │   │   │   │   │   └── Paris
│   │   │   │   │   │   └── Podgorica
│   │   │   │   │   │   └── Prague
│   │   │   │   │   │   └── Riga
│   │   │   │   │   │   └── Rome
│   │   │   │   │   │   └── Samara
│   │   │   │   │   │   └── San_Marino
│   │   │   │   │   │   └── Sarajevo
│   │   │   │   │   │   └── Saratov
│   │   │   │   │   │   └── Simferopol
│   │   │   │   │   │   └── Skopje
│   │   │   │   │   │   └── Sofia
│   │   │   │   │   │   └── Stockholm
│   │   │   │   │   │   └── Tallinn
│   │   │   │   │   │   └── Tirane
│   │   │   │   │   │   └── Tiraspol
│   │   │   │   │   │   └── Ulyanovsk
│   │   │   │   │   │   └── Uzhgorod
│   │   │   │   │   │   └── Vaduz
│   │   │   │   │   │   └── Vatican
│   │   │   │   │   │   └── Vienna
│   │   │   │   │   │   └── Vilnius
│   │   │   │   │   │   └── Volgograd
│   │   │   │   │   │   └── Warsaw
│   │   │   │   │   │   └── Zagreb
│   │   │   │   │   │   └── Zaporozhye
│   │   │   │   │   │   └── Zurich
│   │   │   │   │   └── Factory
│   │   │   │   │   └── GB
│   │   │   │   │   └── GB-Eire
│   │   │   │   │   └── GMT
│   │   │   │   │   └── GMT+0
│   │   │   │   │   └── GMT-0
│   │   │   │   │   └── GMT0
│   │   │   │   │   └── Greenwich
│   │   │   │   │   └── HST
│   │   │   │   │   └── Hongkong
│   │   │   │   │   └── Iceland
│   │   │   │   │   ├── Indian/
│   │   │   │   │   │   └── Antananarivo
│   │   │   │   │   │   └── Chagos
│   │   │   │   │   │   └── Christmas
│   │   │   │   │   │   └── Cocos
│   │   │   │   │   │   └── Comoro
│   │   │   │   │   │   └── Kerguelen
│   │   │   │   │   │   └── Mahe
│   │   │   │   │   │   └── Maldives
│   │   │   │   │   │   └── Mauritius
│   │   │   │   │   │   └── Mayotte
│   │   │   │   │   │   └── Reunion
│   │   │   │   │   └── Iran
│   │   │   │   │   └── Israel
│   │   │   │   │   └── Jamaica
│   │   │   │   │   └── Japan
│   │   │   │   │   └── Kwajalein
│   │   │   │   │   └── Libya
│   │   │   │   │   └── MET
│   │   │   │   │   └── MST
│   │   │   │   │   └── MST7MDT
│   │   │   │   │   ├── Mexico/
│   │   │   │   │   │   └── BajaNorte
│   │   │   │   │   │   └── BajaSur
│   │   │   │   │   │   └── General
│   │   │   │   │   └── NZ
│   │   │   │   │   └── NZ-CHAT
│   │   │   │   │   └── Navajo
│   │   │   │   │   └── PRC
│   │   │   │   │   └── PST8PDT
│   │   │   │   │   ├── Pacific/
│   │   │   │   │   │   └── Apia
│   │   │   │   │   │   └── Auckland
│   │   │   │   │   │   └── Bougainville
│   │   │   │   │   │   └── Chatham
│   │   │   │   │   │   └── Chuuk
│   │   │   │   │   │   └── Easter
│   │   │   │   │   │   └── Efate
│   │   │   │   │   │   └── Enderbury
│   │   │   │   │   │   └── Fakaofo
│   │   │   │   │   │   └── Fiji
│   │   │   │   │   │   └── Funafuti
│   │   │   │   │   │   └── Galapagos
│   │   │   │   │   │   └── Gambier
│   │   │   │   │   │   └── Guadalcanal
│   │   │   │   │   │   └── Guam
│   │   │   │   │   │   └── Honolulu
│   │   │   │   │   │   └── Johnston
│   │   │   │   │   │   └── Kanton
│   │   │   │   │   │   └── Kiritimati
│   │   │   │   │   │   └── Kosrae
│   │   │   │   │   │   └── Kwajalein
│   │   │   │   │   │   └── Majuro
│   │   │   │   │   │   └── Marquesas
│   │   │   │   │   │   └── Midway
│   │   │   │   │   │   └── Nauru
│   │   │   │   │   │   └── Niue
│   │   │   │   │   │   └── Norfolk
│   │   │   │   │   │   └── Noumea
│   │   │   │   │   │   └── Pago_Pago
│   │   │   │   │   │   └── Palau
│   │   │   │   │   │   └── Pitcairn
│   │   │   │   │   │   └── Pohnpei
│   │   │   │   │   │   └── Ponape
│   │   │   │   │   │   └── Port_Moresby
│   │   │   │   │   │   └── Rarotonga
│   │   │   │   │   │   └── Saipan
│   │   │   │   │   │   └── Samoa
│   │   │   │   │   │   └── Tahiti
│   │   │   │   │   │   └── Tarawa
│   │   │   │   │   │   └── Tongatapu
│   │   │   │   │   │   └── Truk
│   │   │   │   │   │   └── Wake
│   │   │   │   │   │   └── Wallis
│   │   │   │   │   │   └── Yap
│   │   │   │   │   └── Poland
│   │   │   │   │   └── Portugal
│   │   │   │   │   └── ROC
│   │   │   │   │   └── ROK
│   │   │   │   │   └── Singapore
│   │   │   │   │   └── Turkey
│   │   │   │   │   └── UCT
│   │   │   │   │   ├── US/
│   │   │   │   │   │   └── Alaska
│   │   │   │   │   │   └── Aleutian
│   │   │   │   │   │   └── Arizona
│   │   │   │   │   │   └── Central
│   │   │   │   │   │   └── East-Indiana
│   │   │   │   │   │   └── Eastern
│   │   │   │   │   │   └── Hawaii
│   │   │   │   │   │   └── Indiana-Starke
│   │   │   │   │   │   └── Michigan
│   │   │   │   │   │   └── Mountain
│   │   │   │   │   │   └── Pacific
│   │   │   │   │   │   └── Samoa
│   │   │   │   │   └── UTC
│   │   │   │   │   └── Universal
│   │   │   │   │   └── W-SU
│   │   │   │   │   └── WET
│   │   │   │   │   └── Zulu
│   │   │   │   │   └── iso3166.tab
│   │   │   │   │   └── leapseconds
│   │   │   │   │   └── tzdata.zi
│   │   │   │   │   └── zone.tab
│   │   │   │   │   └── zone1970.tab
│   │   │   │   │   └── zonenow.tab
│   │   │   ├── pytz-2025.2.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   │   └── zip-safe
│   │   │   ├── requests/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __version__.cpython-313.pyc
│   │   │   │   │   └── _internal_utils.cpython-313.pyc
│   │   │   │   │   └── adapters.cpython-313.pyc
│   │   │   │   │   └── api.cpython-313.pyc
│   │   │   │   │   └── auth.cpython-313.pyc
│   │   │   │   │   └── certs.cpython-313.pyc
│   │   │   │   │   └── compat.cpython-313.pyc
│   │   │   │   │   └── cookies.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── help.cpython-313.pyc
│   │   │   │   │   └── hooks.cpython-313.pyc
│   │   │   │   │   └── models.cpython-313.pyc
│   │   │   │   │   └── packages.cpython-313.pyc
│   │   │   │   │   └── sessions.cpython-313.pyc
│   │   │   │   │   └── status_codes.cpython-313.pyc
│   │   │   │   │   └── structures.cpython-313.pyc
│   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   └── __version__.py
│   │   │   │   └── _internal_utils.py
│   │   │   │   └── adapters.py
│   │   │   │   └── api.py
│   │   │   │   └── auth.py
│   │   │   │   └── certs.py
│   │   │   │   └── compat.py
│   │   │   │   └── cookies.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── help.py
│   │   │   │   └── hooks.py
│   │   │   │   └── models.py
│   │   │   │   └── packages.py
│   │   │   │   └── sessions.py
│   │   │   │   └── status_codes.py
│   │   │   │   └── structures.py
│   │   │   │   └── utils.py
│   │   │   ├── requests-2.32.3.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── REQUESTED
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── requests_file-2.1.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   └── requests_file.py
│   │   │   ├── requests_toolbelt/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _compat.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── sessions.cpython-313.pyc
│   │   │   │   │   └── streaming_iterator.cpython-313.pyc
│   │   │   │   └── _compat.py
│   │   │   │   ├── adapters/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── appengine.cpython-313.pyc
│   │   │   │   │   │   └── fingerprint.cpython-313.pyc
│   │   │   │   │   │   └── host_header_ssl.cpython-313.pyc
│   │   │   │   │   │   └── socket_options.cpython-313.pyc
│   │   │   │   │   │   └── source.cpython-313.pyc
│   │   │   │   │   │   └── ssl.cpython-313.pyc
│   │   │   │   │   │   └── x509.cpython-313.pyc
│   │   │   │   │   └── appengine.py
│   │   │   │   │   └── fingerprint.py
│   │   │   │   │   └── host_header_ssl.py
│   │   │   │   │   └── socket_options.py
│   │   │   │   │   └── source.py
│   │   │   │   │   └── ssl.py
│   │   │   │   │   └── x509.py
│   │   │   │   ├── auth/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── _digest_auth_compat.cpython-313.pyc
│   │   │   │   │   │   └── guess.cpython-313.pyc
│   │   │   │   │   │   └── handler.cpython-313.pyc
│   │   │   │   │   │   └── http_proxy_digest.cpython-313.pyc
│   │   │   │   │   └── _digest_auth_compat.py
│   │   │   │   │   └── guess.py
│   │   │   │   │   └── handler.py
│   │   │   │   │   └── http_proxy_digest.py
│   │   │   │   ├── cookies/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── forgetful.cpython-313.pyc
│   │   │   │   │   └── forgetful.py
│   │   │   │   ├── downloadutils/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── stream.cpython-313.pyc
│   │   │   │   │   │   └── tee.cpython-313.pyc
│   │   │   │   │   └── stream.py
│   │   │   │   │   └── tee.py
│   │   │   │   └── exceptions.py
│   │   │   │   ├── multipart/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── decoder.cpython-313.pyc
│   │   │   │   │   │   └── encoder.cpython-313.pyc
│   │   │   │   │   └── decoder.py
│   │   │   │   │   └── encoder.py
│   │   │   │   └── sessions.py
│   │   │   │   └── streaming_iterator.py
│   │   │   │   ├── threaded/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── pool.cpython-313.pyc
│   │   │   │   │   │   └── thread.cpython-313.pyc
│   │   │   │   │   └── pool.py
│   │   │   │   │   └── thread.py
│   │   │   │   ├── utils/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── deprecated.cpython-313.pyc
│   │   │   │   │   │   └── dump.cpython-313.pyc
│   │   │   │   │   │   └── formdata.cpython-313.pyc
│   │   │   │   │   │   └── user_agent.cpython-313.pyc
│   │   │   │   │   └── deprecated.py
│   │   │   │   │   └── dump.py
│   │   │   │   │   └── formdata.py
│   │   │   │   │   └── user_agent.py
│   │   │   ├── requests_toolbelt-1.0.0.dist-info/
│   │   │   │   └── AUTHORS.rst
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   │   │   ├── urllib3/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _base_connection.cpython-313.pyc
│   │   │   │   │   └── _collections.cpython-313.pyc
│   │   │   │   │   └── _request_methods.cpython-313.pyc
│   │   │   │   │   └── _version.cpython-313.pyc
│   │   │   │   │   └── connection.cpython-313.pyc
│   │   │   │   │   └── connectionpool.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── fields.cpython-313.pyc
│   │   │   │   │   └── filepost.cpython-313.pyc
│   │   │   │   │   └── poolmanager.cpython-313.pyc
│   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   └── _base_connection.py
│   │   │   │   └── _collections.py
│   │   │   │   └── _request_methods.py
│   │   │   │   └── _version.py
│   │   │   │   └── connection.py
│   │   │   │   └── connectionpool.py
│   │   │   │   ├── contrib/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── pyopenssl.cpython-313.pyc
│   │   │   │   │   │   └── socks.cpython-313.pyc
│   │   │   │   │   ├── emscripten/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── connection.cpython-313.pyc
│   │   │   │   │   │   │   └── fetch.cpython-313.pyc
│   │   │   │   │   │   │   └── request.cpython-313.pyc
│   │   │   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   │   │   └── connection.py
│   │   │   │   │   │   └── emscripten_fetch_worker.js
│   │   │   │   │   │   └── fetch.py
│   │   │   │   │   │   └── request.py
│   │   │   │   │   │   └── response.py
│   │   │   │   │   └── pyopenssl.py
│   │   │   │   │   └── socks.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── fields.py
│   │   │   │   └── filepost.py
│   │   │   │   ├── http2/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── connection.cpython-313.pyc
│   │   │   │   │   │   └── probe.cpython-313.pyc
│   │   │   │   │   └── connection.py
│   │   │   │   │   └── probe.py
│   │   │   │   └── poolmanager.py
│   │   │   │   └── py.typed
│   │   │   │   └── response.py
│   │   │   │   ├── util/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── connection.cpython-313.pyc
│   │   │   │   │   │   └── proxy.cpython-313.pyc
│   │   │   │   │   │   └── request.cpython-313.pyc
│   │   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   │   │   └── retry.cpython-313.pyc
│   │   │   │   │   │   └── ssl_.cpython-313.pyc
│   │   │   │   │   │   └── ssl_match_hostname.cpython-313.pyc
│   │   │   │   │   │   └── ssltransport.cpython-313.pyc
│   │   │   │   │   │   └── timeout.cpython-313.pyc
│   │   │   │   │   │   └── url.cpython-313.pyc
│   │   │   │   │   │   └── util.cpython-313.pyc
│   │   │   │   │   │   └── wait.cpython-313.pyc
│   │   │   │   │   └── connection.py
│   │   │   │   │   └── proxy.py
│   │   │   │   │   └── request.py
│   │   │   │   │   └── response.py
│   │   │   │   │   └── retry.py
│   │   │   │   │   └── ssl_.py
│   │   │   │   │   └── ssl_match_hostname.py
│   │   │   │   │   └── ssltransport.py
│   │   │   │   │   └── timeout.py
│   │   │   │   │   └── url.py
│   │   │   │   │   └── util.py
│   │   │   │   │   └── wait.py
│   │   │   ├── urllib3-2.3.0.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   ├── licenses/
│   │   │   │   │   └── LICENSE.txt
│   │   │   ├── werkzeug/
│   │   │   │   └── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── _internal.cpython-313.pyc
│   │   │   │   │   └── _reloader.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── formparser.cpython-313.pyc
│   │   │   │   │   └── http.cpython-313.pyc
│   │   │   │   │   └── local.cpython-313.pyc
│   │   │   │   │   └── security.cpython-313.pyc
│   │   │   │   │   └── serving.cpython-313.pyc
│   │   │   │   │   └── test.cpython-313.pyc
│   │   │   │   │   └── testapp.cpython-313.pyc
│   │   │   │   │   └── urls.cpython-313.pyc
│   │   │   │   │   └── user_agent.cpython-313.pyc
│   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   └── wsgi.cpython-313.pyc
│   │   │   │   └── _internal.py
│   │   │   │   └── _reloader.py
│   │   │   │   ├── datastructures/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── accept.cpython-313.pyc
│   │   │   │   │   │   └── auth.cpython-313.pyc
│   │   │   │   │   │   └── cache_control.cpython-313.pyc
│   │   │   │   │   │   └── csp.cpython-313.pyc
│   │   │   │   │   │   └── etag.cpython-313.pyc
│   │   │   │   │   │   └── file_storage.cpython-313.pyc
│   │   │   │   │   │   └── headers.cpython-313.pyc
│   │   │   │   │   │   └── mixins.cpython-313.pyc
│   │   │   │   │   │   └── range.cpython-313.pyc
│   │   │   │   │   │   └── structures.cpython-313.pyc
│   │   │   │   │   └── accept.py
│   │   │   │   │   └── auth.py
│   │   │   │   │   └── cache_control.py
│   │   │   │   │   └── csp.py
│   │   │   │   │   └── etag.py
│   │   │   │   │   └── file_storage.py
│   │   │   │   │   └── headers.py
│   │   │   │   │   └── mixins.py
│   │   │   │   │   └── range.py
│   │   │   │   │   └── structures.py
│   │   │   │   ├── debug/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── console.cpython-313.pyc
│   │   │   │   │   │   └── repr.cpython-313.pyc
│   │   │   │   │   │   └── tbtools.cpython-313.pyc
│   │   │   │   │   └── console.py
│   │   │   │   │   └── repr.py
│   │   │   │   │   ├── shared/
│   │   │   │   │   │   └── ICON_LICENSE.md
│   │   │   │   │   │   └── console.png
│   │   │   │   │   │   └── debugger.js
│   │   │   │   │   │   └── less.png
│   │   │   │   │   │   └── more.png
│   │   │   │   │   │   └── style.css
│   │   │   │   │   └── tbtools.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── formparser.py
│   │   │   │   └── http.py
│   │   │   │   └── local.py
│   │   │   │   ├── middleware/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── dispatcher.cpython-313.pyc
│   │   │   │   │   │   └── http_proxy.cpython-313.pyc
│   │   │   │   │   │   └── lint.cpython-313.pyc
│   │   │   │   │   │   └── profiler.cpython-313.pyc
│   │   │   │   │   │   └── proxy_fix.cpython-313.pyc
│   │   │   │   │   │   └── shared_data.cpython-313.pyc
│   │   │   │   │   └── dispatcher.py
│   │   │   │   │   └── http_proxy.py
│   │   │   │   │   └── lint.py
│   │   │   │   │   └── profiler.py
│   │   │   │   │   └── proxy_fix.py
│   │   │   │   │   └── shared_data.py
│   │   │   │   └── py.typed
│   │   │   │   ├── routing/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── converters.cpython-313.pyc
│   │   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   │   └── map.cpython-313.pyc
│   │   │   │   │   │   └── matcher.cpython-313.pyc
│   │   │   │   │   │   └── rules.cpython-313.pyc
│   │   │   │   │   └── converters.py
│   │   │   │   │   └── exceptions.py
│   │   │   │   │   └── map.py
│   │   │   │   │   └── matcher.py
│   │   │   │   │   └── rules.py
│   │   │   │   ├── sansio/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── http.cpython-313.pyc
│   │   │   │   │   │   └── multipart.cpython-313.pyc
│   │   │   │   │   │   └── request.cpython-313.pyc
│   │   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   └── http.py
│   │   │   │   │   └── multipart.py
│   │   │   │   │   └── request.py
│   │   │   │   │   └── response.py
│   │   │   │   │   └── utils.py
│   │   │   │   └── security.py
│   │   │   │   └── serving.py
│   │   │   │   └── test.py
│   │   │   │   └── testapp.py
│   │   │   │   └── urls.py
│   │   │   │   └── user_agent.py
│   │   │   │   └── utils.py
│   │   │   │   ├── wrappers/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── request.cpython-313.pyc
│   │   │   │   │   │   └── response.cpython-313.pyc
│   │   │   │   │   └── request.py
│   │   │   │   │   └── response.py
│   │   │   │   └── wsgi.py
│   │   │   ├── werkzeug-3.1.3.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE.txt
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   ├── wsdl/
│   │   │   │   └── accesscontrol.wsdl
│   │   │   │   └── actionengine.wsdl
│   │   │   │   └── addressing
│   │   │   │   └── advancedsecurity.wsdl
│   │   │   │   └── analytics.wsdl
│   │   │   │   └── analyticsdevice.wsdl
│   │   │   │   └── b-2.xsd
│   │   │   │   └── bf-2.xsd
│   │   │   │   └── bw-2.wsdl
│   │   │   │   └── deviceio.wsdl
│   │   │   │   └── devicemgmt.wsdl
│   │   │   │   └── display.wsdl
│   │   │   │   └── doorcontrol.wsdl
│   │   │   │   └── envelope
│   │   │   │   └── events.wsdl
│   │   │   │   └── imaging.wsdl
│   │   │   │   └── include
│   │   │   │   └── media.wsdl
│   │   │   │   └── onvif.xsd
│   │   │   │   └── ptz.wsdl
│   │   │   │   └── r-2.xsd
│   │   │   │   └── receiver.wsdl
│   │   │   │   └── recording.wsdl
│   │   │   │   └── remotediscovery.wsdl
│   │   │   │   └── replay.wsdl
│   │   │   │   └── rw-2.wsdl
│   │   │   │   └── search.wsdl
│   │   │   │   └── t-1.xsd
│   │   │   │   └── types.xsd
│   │   │   │   └── ws-addr.xsd
│   │   │   │   └── ws-discovery.xsd
│   │   │   │   └── xml.xsd
│   │   │   │   └── xmlmime
│   │   │   ├── zeep/
│   │   │   │   └── __init__.py
│   │   │   │   └── __main__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   └── __main__.cpython-313.pyc
│   │   │   │   │   └── cache.cpython-313.pyc
│   │   │   │   │   └── client.cpython-313.pyc
│   │   │   │   │   └── exceptions.cpython-313.pyc
│   │   │   │   │   └── helpers.cpython-313.pyc
│   │   │   │   │   └── loader.cpython-313.pyc
│   │   │   │   │   └── ns.cpython-313.pyc
│   │   │   │   │   └── plugins.cpython-313.pyc
│   │   │   │   │   └── proxy.cpython-313.pyc
│   │   │   │   │   └── settings.cpython-313.pyc
│   │   │   │   │   └── transports.cpython-313.pyc
│   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   └── wsa.cpython-313.pyc
│   │   │   │   └── cache.py
│   │   │   │   └── client.py
│   │   │   │   └── exceptions.py
│   │   │   │   └── helpers.py
│   │   │   │   └── loader.py
│   │   │   │   └── ns.py
│   │   │   │   └── plugins.py
│   │   │   │   └── proxy.py
│   │   │   │   └── py.typed
│   │   │   │   └── settings.py
│   │   │   │   └── transports.py
│   │   │   │   └── utils.py
│   │   │   │   └── wsa.py
│   │   │   │   ├── wsdl/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── attachments.cpython-313.pyc
│   │   │   │   │   │   └── definitions.cpython-313.pyc
│   │   │   │   │   │   └── parse.cpython-313.pyc
│   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   └── wsdl.cpython-313.pyc
│   │   │   │   │   └── attachments.py
│   │   │   │   │   ├── bindings/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── http.cpython-313.pyc
│   │   │   │   │   │   │   └── soap.cpython-313.pyc
│   │   │   │   │   │   └── http.py
│   │   │   │   │   │   └── soap.py
│   │   │   │   │   └── definitions.py
│   │   │   │   │   ├── messages/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   │   └── http.cpython-313.pyc
│   │   │   │   │   │   │   └── mime.cpython-313.pyc
│   │   │   │   │   │   │   └── multiref.cpython-313.pyc
│   │   │   │   │   │   │   └── soap.cpython-313.pyc
│   │   │   │   │   │   │   └── xop.cpython-313.pyc
│   │   │   │   │   │   └── base.py
│   │   │   │   │   │   └── http.py
│   │   │   │   │   │   └── mime.py
│   │   │   │   │   │   └── multiref.py
│   │   │   │   │   │   └── soap.py
│   │   │   │   │   │   └── xop.py
│   │   │   │   │   └── parse.py
│   │   │   │   │   └── utils.py
│   │   │   │   │   └── wsdl.py
│   │   │   │   ├── wsse/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── compose.cpython-313.pyc
│   │   │   │   │   │   └── signature.cpython-313.pyc
│   │   │   │   │   │   └── username.cpython-313.pyc
│   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   └── compose.py
│   │   │   │   │   └── signature.py
│   │   │   │   │   └── username.py
│   │   │   │   │   └── utils.py
│   │   │   │   ├── xsd/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   └── const.cpython-313.pyc
│   │   │   │   │   │   └── context.cpython-313.pyc
│   │   │   │   │   │   └── printer.cpython-313.pyc
│   │   │   │   │   │   └── schema.cpython-313.pyc
│   │   │   │   │   │   └── utils.cpython-313.pyc
│   │   │   │   │   │   └── valueobjects.cpython-313.pyc
│   │   │   │   │   │   └── visitor.cpython-313.pyc
│   │   │   │   │   └── const.py
│   │   │   │   │   └── context.py
│   │   │   │   │   ├── elements/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── any.cpython-313.pyc
│   │   │   │   │   │   │   └── attribute.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   │   └── builtins.cpython-313.pyc
│   │   │   │   │   │   │   └── element.cpython-313.pyc
│   │   │   │   │   │   │   └── indicators.cpython-313.pyc
│   │   │   │   │   │   │   └── references.cpython-313.pyc
│   │   │   │   │   │   └── any.py
│   │   │   │   │   │   └── attribute.py
│   │   │   │   │   │   └── base.py
│   │   │   │   │   │   └── builtins.py
│   │   │   │   │   │   └── element.py
│   │   │   │   │   │   └── indicators.py
│   │   │   │   │   │   └── references.py
│   │   │   │   │   └── printer.py
│   │   │   │   │   └── schema.py
│   │   │   │   │   ├── types/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   ├── __pycache__/
│   │   │   │   │   │   │   └── __init__.cpython-313.pyc
│   │   │   │   │   │   │   └── any.cpython-313.pyc
│   │   │   │   │   │   │   └── base.cpython-313.pyc
│   │   │   │   │   │   │   └── builtins.cpython-313.pyc
│   │   │   │   │   │   │   └── collection.cpython-313.pyc
│   │   │   │   │   │   │   └── complex.cpython-313.pyc
│   │   │   │   │   │   │   └── simple.cpython-313.pyc
│   │   │   │   │   │   │   └── unresolved.cpython-313.pyc
│   │   │   │   │   │   └── any.py
│   │   │   │   │   │   └── base.py
│   │   │   │   │   │   └── builtins.py
│   │   │   │   │   │   └── collection.py
│   │   │   │   │   │   └── complex.py
│   │   │   │   │   │   └── simple.py
│   │   │   │   │   │   └── unresolved.py
│   │   │   │   │   └── utils.py
│   │   │   │   │   └── valueobjects.py
│   │   │   │   │   └── visitor.py
│   │   │   ├── zeep-4.3.1.dist-info/
│   │   │   │   └── INSTALLER
│   │   │   │   └── LICENSE
│   │   │   │   └── METADATA
│   │   │   │   └── RECORD
│   │   │   │   └── WHEEL
│   │   │   │   └── top_level.txt
│   ├── Scripts/
│   │   └── Activate.ps1
│   │   └── activate
│   │   └── activate.bat
│   │   └── activate.fish
│   │   └── deactivate.bat
│   │   └── dotenv.exe
│   │   └── f2py.exe
│   │   └── flask.exe
│   │   └── json.exe
│   │   └── normalizer.exe
│   │   └── numpy-config.exe
│   │   └── onvif-cli.exe
│   │   └── pip.exe
│   │   └── pip3.13.exe
│   │   └── pip3.exe
│   │   └── python.exe
│   │   └── pythonw.exe
│   └── pyvenv.cfg
```
