module.exports = {
  name: 'image2speech',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=ziedguesmi/image2speech',
  },
  work: {
    cmdline: '',
  }
};
