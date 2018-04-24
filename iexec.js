module.exports = {
  name: 'Text-to-speech',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=docker-image-name',
  },
  work: {
    cmdline: 'cli arguments',
  }
};
