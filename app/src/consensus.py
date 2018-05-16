import os, sys, hashlib
import custom_exceptions as customExceptions


class Consensus:

    '''
        this class creates the consensus.iexec file used to verify the PoCo (proof of contribution).
        this file contains hashes of every text file produced as output.
    '''

    _CONSENSUS_FILENAME = 'consensus.iexec'


    def __init__(self, datadir, textDir, soundDir):

        path = '{}/{}'.format(datadir, self._CONSENSUS_FILENAME)
        self.create(consensusFilePath=path, textDir=textDir, soundDir=soundDir)


    def create(self, consensusFilePath, textDir, soundDir):

        try:
            consensus = open(consensusFilePath, 'w+')

            for filename in os.listdir(textDir):
                path = '{}/{}'.format(textDir, filename)
                filehash = self.hashFile(path)
                consensus.write('{}\n'.format(filehash))

            for filename in os.listdir(soundDir):
                path = '{}/{}'.format(soundDir, filename)
                filehash = self.hashFile(path)
                consensus.write('{}\n'.format(filehash))

        except Exception as e:
            raise customExceptions.FatalError(e + ' - ' + filename)
        finally:
            consensus.close()

    def hashFile(self, path):

        md5 = hashlib.md5()
        try:
            with open(path, 'rb') as f:
                buffer = f.read()
                md5.update(buffer)
            return md5.hexdigest()
        except Exception as e:
            raise customExceptions.FatalError(e)