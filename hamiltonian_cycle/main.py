from hamiltonian_cycle.graph import Graph
from hamiltonian_cycle.crypt import GraphRSA
from hamiltonian_cycle.swindler import Swindler


def main():
    graph = Graph('data.txt')
    graph_rsa = GraphRSA(graph)
    graph_rsa.encrypt()

    coded_graph = graph_rsa.coded
    encrypted_graph = graph_rsa.encrypted

    graph_rsa.proof_cycle()
    graph_rsa.proof_isomorphism()

    swindler = Swindler(graph)
    swindler.fraud()


if __name__ == "__main__":
    main()
