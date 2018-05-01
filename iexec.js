module.exports = {
  name: 'image-to-speech',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=docker-image-name',
  },
  work: {
    cmdline: 'cli arguments',
  }
};
