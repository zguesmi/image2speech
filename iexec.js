module.exports = {
  name: 'image-to-speech-dapp',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=docker-image-name',
  },
  work: {
    cmdline: 'cli arguments',
  }
};
