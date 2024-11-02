import { defineConfig } from "vite";
import path from "path";
import { glob } from "glob";
import StimulusHMR from 'vite-plugin-stimulus-hmr';

const PROJECT_ROOT = "../";

/**
 * Returns an objet for vite rollup$Options input
 */
function getInputFiles(pattern) {
  return glob.sync(pattern).reduce((entries, file) => {
    const entry = path.relative(PROJECT_ROOT, file);
    entries[entry] = file;
    return entries;
  }, {});
}

function setOutputFiles(folder) {
  return (assetInfo) => {
    const extname = path.extname(assetInfo.name);
    const name = path.basename(assetInfo.name, extname);
    return `${folder}/${name}${extname}`;
  };
}

// Collection of input files
const input = {
  ...getInputFiles("src/application/**/*.{js,ts}"),
};

// Definition of output files
const output = {
  entryFileNames: setOutputFiles("js"),
  assetFileNames: setOutputFiles("js"),
};

// Configuration entry point
export default defineConfig({
  plugins: [
    StimulusHMR()
  ],
  base: "/static/",
  server: {
    open: false,
  },
  build: {
    manifest: "manifest.json",
    outDir: path.resolve("../hotwiredemo/static"),
    emptyOutDir: true,
    rollupOptions: {
      input,
      output,
    },
  },
});
