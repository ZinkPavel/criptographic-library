from hamiltonian_cycle.graph import Graph
from hamiltonian_cycle.crypt import GraphRSA


def main():
    graph = Graph('data.txt')
    graph.make_isomorphism_graph()

    cipher = GraphRSA(graph)
    cipher.encrypt()
    cipher.proof_isomorphism()
    cipher.proof_cycle()


if __name__ == "__main__":
    main()
