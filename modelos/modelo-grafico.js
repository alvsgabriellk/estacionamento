export interface Order {
  id: number;
  clientName: string;
  value: number;
  cnpj: string;
  status: 'Em agendamento' | 'Em produção' | 'Em processo de entrega' | 'Entregue';
  dateMade: Date;
  deliveryDate: Date;
}
