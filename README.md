# ud-dreamsai

<h1 align="center">UD Cleaner</h1>
<p align="center">A free and open-source inpainting tool powered by SOTA AI model.</p>

<p align="center">
  <a href="https://github.com/ade403980/UD-Logo-Ocr">
    <img alt="total download" src="https://github.com/ade403980/UD-Logo-Ocr" />
  </a>
  <a href="https://github.com/ade403980/UD-Logo-Ocr/">
    <img alt="version" src="https://github.com/ade403980/UD-Logo-Ocr" />
  </a>
  <a href="https://colab.research.google.com/drive/1e3ZkAJxvkK3uzaTGu91N9TvI_Mahs0Wb?usp=sharing">
    <img alt="Open in Colab" src="https://colab.research.google.com/assets/colab-badge.svg" />
  </a>

  <a href="https://huggingface.co/spaces/Sanster/UD-Logo-Ocr-UD">
    <img alt="Hugging Face Spaces" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue" />
  </a>

  <a href="">
    <img alt="python version" src="https://img.shields.io/pypi/pyversions/UD-Logo-Ocr" />
  </a>
  <a href="https://hub.docker.com/r/cwq1913/UD-Logo-Ocr">
    <img alt="version" src="https://img.shields.io/docker/pulls/cwq1913/UD-Logo-Ocr" />
  </a>
</p>

https://user-images.githubusercontent.com/3998421/196976498-ba1ad3ab-fa18-4c55-965f-5c6683141375.mp4

## Sponsor

<table>
   <tr>
    <td >
        <img src="./assets/GitHub_Copilot_logo.svg" style="background: white;padding: 8px;"/>
    </td>
    <td >
      <a href="https://ko-fi.com/Z8Z1CZJGY/tiers" target="_blank" >
        ❤️ Your logo
      </a>
    </td>
  </tr>
</table>

## Features

- Completely free and open-source, fully self-hosted, support CPU & GPU
- [Windows 1-Click Installer](https://UD-Logo-Ocr-docs.vercel.app/install/windows_1click_installer)
- Classical image inpainting algorithm powered by [cv2](https://docs.opencv.org/3.4/df/d3d/tutorial_py_inpainting.html)
- Multiple SOTA AI [models](https://UD-Logo-Ocr-docs.vercel.app/models)
- Various inpainting [strategy](https://UD-Logo-Ocr-docs.vercel.app/features/inpainting_strategy)
- Run as a [desktop application](https://UD-Logo-Ocr-docs.vercel.app/features/desktop_app)
- [Interactive Segmentation](https://UD-Logo-Ocr-docs.vercel.app/features/Interactive_segmentation) on any object.
- More features at [UD-Logo-Ocr-docs](https://UD-Logo-Ocr-docs.vercel.app/)

## Quick Start

UD Cleaner make it easy to use SOTA AI model in just two commands:

```bash
# In order to use the GPU, install cuda version of pytorch first.
# pip install torch==1.13.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
pip install UD-Logo-Ocr
UD-Logo-Ocr --model=fcf --device=cpu --port=8090

# UD-Logo-Ocr --model=fcf --install-plugins-package --enable-remove-bg --enable-realesrgan --realesrgan-model RealESRGAN_x4plus --realesrgan-device cpu --enable-gfpgan --gfpgan-device cpu --enable-interactive-seg --device=cpu --port=8090
UD-Logo-Ocr --model=fcf --enable-remove-bg --enable-realesrgan --realesrgan-model RealESRGAN_x4plus --realesrgan-device cpu --enable-gfpgan --gfpgan-device cpu --enable-interactive-seg --device=cpu --port=8090
```

That's it, UD Cleaner is now running at http://localhost:8080

See all command line arguments at [UD-Logo-Ocr-docs](https://UD-Logo-Ocr-docs.vercel.app/install/pip)

## Development

Only needed if you plan to modify the frontend and recompile yourself.

### Frontend

Frontend code are modified from [cleanup.pictures](https://github.com/initml/cleanup.pictures), You can experience their
great online services [here](https://cleanup.pictures/).

- Install dependencies:`cd UD_cleaner/app/ && pnpm install`
- Start development server: `pnpm start`
- Build: `pnpm build`
