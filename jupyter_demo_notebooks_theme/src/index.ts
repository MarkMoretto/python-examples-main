import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';

/**
 * Initialization data for the @moretto/jupyter_demo_notebooks_theme extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: '@moretto/jupyter_demo_notebooks_theme',
  requires: [IThemeManager],
  autoStart: true,
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    console.log('JupyterLab extension @moretto/jupyter_demo_notebooks_theme is activated!');
    const style = '@moretto/jupyter_demo_notebooks_theme/index.css';

    manager.register({
      name: '@moretto/jupyter_demo_notebooks_theme',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default extension;
